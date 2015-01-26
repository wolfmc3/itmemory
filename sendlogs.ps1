Param (
    [Parameter(Mandatory=$true)]
    [string]$hwid,
    [string]$ftphost = "192.168.10.3",
    [string]$port = "2121",
    [string]$user = "admin",
    [string]$password = "admin",
    [string]$logpath = $env:TEMP + "\sendlogs"
)

$def = @"
public class ActiveFtpWebClient : System.Net.WebClient
{
  protected override System.Net.WebRequest GetWebRequest(System.Uri address)
  {
    System.Net.WebRequest request = base.GetWebRequest(address);
    if (request is System.Net.FtpWebRequest)
    {
      (request as System.Net.FtpWebRequest).UsePassive = false;
    }
    return request;
  }
}
"@

Add-Type -TypeDefinition $def

function SendToFtp($sendfile) {
    
    $ftp = "ftp://${ftphost}:${port}/";
    Write-Host -Object "Ftp url: $ftp";

    $webclient = New-Object ActiveFtpWebClient;
    $webclient.Credentials = New-Object System.Net.NetworkCredential($user,$password)
    $uri = New-Object -TypeName System.Uri -ArgumentList ($ftp + $sendfile.Name) ;
    Write-Host -Object ("Uploading " + $sendfile.FullName + "...");
    $sended = $true
    Try {
        Set-Location -Path $logpath
        $webclient.UploadFile($uri, $sendfile.FullName);
    }
    Catch {
        $err = $_.Exception;
        Write-Host -Object $err;
        $sended = $false
    }
    return $sended
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

$events = Get-WinEvent -FilterHashtable @{logname='*';Level=1,2,3; StartTime=$lastlog}
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

$filesToSend = Get-Item "$logpath\hw-$hwid-log*.csv"

foreach ($fileToSend in $filesToSend) {
    $ret = SendToFtp($fileToSend); 
    if ($ret) {
        $fileToSend.Delete()
    } else {
        break;
        return 0
    }
}