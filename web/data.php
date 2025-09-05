<?php
    // Run the Node.js scraper and output the result
    $output = shell_exec('node ' . __DIR__ . '/scrapee.js');
    echo "Remaining GB: " . htmlspecialchars(trim($output));
?>