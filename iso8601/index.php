<?php

$tz = 'Asia/Tokyo';
date_default_timezone_set($tz);

echo "ISO 8601 datetime format of now (timezone = $tz): " . date('c');
