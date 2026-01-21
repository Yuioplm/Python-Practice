Import-Csv "scores.csv" | ForEach-Object {
    $name = $_.name
    $score = [int]$_.score

    if ($score -ge 80) {
        Write-Output "$name : Excellent"
    }
    elseif ($score -ge 60) {
        Write-Output "$name : Pass"        
    }
    else {
        Write-Output "$name : Fail"
    }
}

