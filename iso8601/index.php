<?php

if (isset($_GET['tz'])) {
    $tz = $_GET['tz'];
} else {
    $tz = 'UTC';
}

date_default_timezone_set($tz);

header('Content-Type: text/plain');

echo date('c') . " (tz = $tz)\n";
