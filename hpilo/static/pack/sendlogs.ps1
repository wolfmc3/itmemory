Param (
    [Parameter(Mandatory=$true)]
    [string]$hwid,
    [string]$remotehost = "remote.globit.it",
    [string]$port = "8081",
    [string]$user = "admin",
    [string]$password = "admin",
    [switch]$ILO,
    [string]$ILOserver = "{ILOIP}",
    [string]$ILOuser = "{ILOUSER}",
    [string]$ILOpassword = "{ILOPASSWORD}",
    [string]$logpath = $env:TEMP + "\sendlogs",
    [string]$token = "",
    [string]$ILOtoken = $token,
    [string]$ILOhwid = $hwid
)

function SendFileHttp($item,$model, $hwid, $token) {
    $wc = new-object System.Net.WebClient

    $enc = [System.Text.Encoding]::ASCII

    $url = "http://${remotehost}:${port}/$model/upload/$hwid/$token";
    Write-Host -object $url
    Write-Host -object $item.FullName
    $resp = $enc.GetBytes("False")
    $resp = $wc.UploadFile($url, $item.FullName )
    if ($enc.GetString($resp) -eq "True") {
        Write-Host -object "file inviato"
        $item.Delete()
    }
}

$logfile = "hw-$hwid-log.csv"


if (Test-Path $logpath) {
    "Current folder $logpath : OK"
} else {
    "Create folder $logpath"
    mkdir $logpath;
}
Set-Location -Path $logpath
$lastlog = (Get-Date).AddHours(-4)
if (Test-Path "$logpath\lastdate.xml") {
    $lastlog = Import-Clixml "$logpath\lastdate.xml"
}

if (Test-Path "$logpath\$logfile") {
    $fl = Get-Item "$logpath\$logfile"
    $c = 1
    while (Test-Path "$logpath\hw-$hwid-log-$c.csv") {
        Write-Output "$logpath\hw-$hwid-log-$c.csv"
        $c = $c + 1;
    }
    $fl.MoveTo("$logpath\hw-$hwid-log-$c.csv");
}

Write-Host -object "Recupero eventi da: $lastlog" 
$logs = (Get-WinEvent -ListLog *).LogName
$splits = [Math]::Ceiling($logs.Length / 256)
$numberOfLogs = $logs.length
$sets = ForEach($i in (1..$splits)){
    $start = ($i - 1)*256
    If($i -eq $splits) {
        $end = $logs.length
    } Else {
        $end = $i * 255
    }
    ,$logs[$start..$end]
}

$events = ForEach($set in $sets) {
    Get-WinEvent -FilterHashtable @{logname=$set;Level=1,2,3,4; StartTime=$lastlog}
}

$lastlog = ($events | measure TimeCreated -Maximum).Maximum

$events = $events | Select-Object Message,Id,Level,RecordId,ProviderName,LogName,@{Name="TimeCreated";Expression={$_.TimeCreated.ToString("yyyy-MM-dd HH:mm")}} 
$events | Export-Csv "$logpath\$logfile" -NoTypeInformation -Encoding ASCII
"Saved export to: " + "$logpath\$logfile"

if ($events.Count -gt 0) {
    $lastlog | Export-Clixml "$logpath\lastdate.xml"
    "New events: " + $events.Count.ToString()
} else {
    (Get-Item $logfile).Delete()
    Write-Host -Object "Nothing to upload. Exit";
}

if ($ILO.IsPresent) {
    c:\GetILOStatus.ps1 -Server $ILOserver -Password $ILOpassword -Username $ILOuser -logfile "$logpath\hw-$hwid-status.json"
}

$filesToSend = Get-Item "$logpath\hw-$hwid-log*.csv"

foreach ($fileToSend in $filesToSend) {
       SendFileHttp $fileToSend "hwlogs" $hwid $token
}

$filesToSend = Get-Item "$logpath\hw-$ILOhwid-status*.json"

foreach ($fileToSend in $filesToSend) {
       SendFileHttp $fileToSend "hpilo" $ILOhwid $ILOtoken
}
