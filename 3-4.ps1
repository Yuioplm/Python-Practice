$excellent = 0
$passed = 0
$failed = 0

Import-Csv ".\scores.csv" | ForEach-Object {
    $score = [int]$_.score

    if ($score -ge 80) {
        $excellent += 1
    }
    elseif($score -ge 60) {
        $passed += 1
    }
    else {
        $failed += 1
    }
}

$result = @(
    [PSCustomObject]@{ Category = "Excellent"; Count = $excellent}
    [PSCustomObject]@{ Category = "Pass"; Count = $passed}
    [PSCustomObject]@{ Category = "Fail"; Count = $failed}
)

$result | Export-Csv result.csv -NoTypeInformation