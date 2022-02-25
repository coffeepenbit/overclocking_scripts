$gaming_oc = Read-Host "Apply gaming OC profile? (y/[n])?"

if($gaming_oc -eq 'y') {
    Push-Location $PSScriptRoot
    Powershell.exe -File reset_gpu.ps1 -NoRestart
    reg import apply_gaming_power_play.reg
    restart64 /q
    overdriventool -c0"gaming"
    Pop-Location
}
pause
