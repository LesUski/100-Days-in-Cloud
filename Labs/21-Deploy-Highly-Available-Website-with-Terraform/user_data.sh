#!/bin/bash
cat > /var/www/html/index.php <<'END'
<?php
$instance_id = file_get_contents("http://instance-data/latest/meta-data/instance-id");
echo "You've reached instance ", $instance_id, "\n";
?>