<?php
    
    $output = shell_exec('node readusage.js');
    echo "<pre>" . htmlspecialchars(trim($output)) . "</pre>";

?>
