[CmdletBinding()]
param(
    [Parameter(Mandatory=$false)]
    [Switch]$NoRestart
)

Add-Type -AssemblyName PresentationCore,PresentationFramework
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if($currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator) -eq $false){
    [System.Windows.MessageBox]::Show('Must run {0} as admin' -f $PSCommandPath)
} else {
    Write-Output $PSScriptRoot
    Push-Location $PSScriptRoot
    # Reset to stock GPU settings to avoid crash after resetting power play table
    OverdriveNTool -c0"stock w/ fan curve"
    reg import delete_power_play.reg

    if($NoRestart -eq $false)
     {
         restart64 /q
     }
    Pop-Location
}
