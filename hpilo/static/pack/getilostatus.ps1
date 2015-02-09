param (
    [string]$Server = "{ILOIP}", 
    [string]$Username = "{ILOUSER}",
    [string]$Password = "{ILOPASSWORD}",
    [string]$logfile = "c:\logs\health.json"
)

$results = @{}

Set-HPiLOUIDStatus -Username $Username -Password $Password -Server $Server -UIDControl On 

$results.SUMMARY = Get-HPiLOHealthSummary -Username $Username -Password $Password -Server $Server 

$temp = Get-HPiLOTemperature -Username $Username -Password $Password -Server $Server

$results.TEMP = $temp.TEMP | where-object { $_.STATUS -notcontains "Not installed"  }

$fans = Get-HPiLOFan -Username $Username -Password $Password -Server $Server

$results.FAN = $fans.FAN | where-object { $_.STATUS -notcontains "Not installed"  } 

$results.LOGICAL_DRIVE = Get-HPiLOStorageController -Username $Username -Password $Password -Server $Server 

$results.LOGICAL_DRIVE = $results.LOGICAL_DRIVE.CONTROLLER.LOGICAL_DRIVE

$results | ConvertTo-Json -Depth 999 | Out-File $logfile

Set-HPiLOUIDStatus -Username $Username -Password $Password -Server $Server -UIDControl Off

