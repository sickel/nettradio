<?php

if($_GET['kanal']=='kanal'){
	returnkanal();
}

$line = '';
$file='/tmp/radiotitle';

$f = fopen($file , 'r');
$cursor = -1;

fseek($f, $cursor, SEEK_END);
$char = fgetc($f);

/**
 * Trim trailing newline chars of the file
 */
while ($char === "\n" || $char === "\r") {
    fseek($f, $cursor--, SEEK_END);
    $char = fgetc($f);
}

/**
 * Read until the start of file or first newline char
 */
while ($char !== false && $char !== "\n" && $char !== "\r") {
    /**
     * Prepend the new char
     */
    $line = $char . $line;
    fseek($f, $cursor--, SEEK_END);
    $char = fgetc($f);
}
$exp=explode('=',$line,2);
$line=ltrim($exp[1],"'");
$line=rtrim($line,"';");

$ret->text=$line;

$file = fopen('/var/www/html/ch.txt',"r");
$ret->ch = fgets($file);

echo json_encode($ret);



?>
