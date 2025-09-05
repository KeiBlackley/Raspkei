<?php
// Run the Python script and capture output
$output = shell_exec('python3 /home/kei/Raspkei/py/batt_stats.py 2>&1');
$stats = json_decode($output, true);
// Debug output for troubleshooting
if (!$stats) {
    echo '<pre>Python output: ' . htmlspecialchars($output) . '</pre>';
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Battery Stats</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f4; text-align: center; padding-top: 50px; }
        .stat { font-size: 1.5em; margin: 10px 0; }
    </style>
</head>
<body>
    <h1>Battery Stats</h1>
    <?php if ($stats): ?>
        <div class="stat">Load Voltage: <strong><?= $stats['load_voltage'] ?> V</strong></div>
        <div class="stat">Shunt Voltage: <strong><?= $stats['shunt_voltage'] ?> V</strong></div>
        <div class="stat">Current: <strong><?= $stats['current'] ?> A</strong></div>
        <div class="stat">Power: <strong><?= $stats['power'] ?> W</strong></div>
        <div class="stat">Percent: <strong><?= $stats['percent'] ?>%</strong></div>
    <?php else: ?>
        <div class="stat">Error reading battery stats.</div>
    <?php endif; ?>
</body>
</html>

