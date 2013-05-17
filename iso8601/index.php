<?php

if (isset($_GET['tz'])) {
    $tz = $_GET['tz'];
} else {
    $tz = 'Asia/Tokyo';
}
echo "tz = $tz\n";

date_default_timezone_set($tz);

echo date('c');
