<?php

$ch=$_GET['ch'];
// echo($ch);
echo('<br/>');
$chs=array(
'p1'=>'http://lyd.nrk.no/nrk_radio_p1_ostlandssendingen_mp3_h',
'p2'=>'http://lyd.nrk.no/nrk_radio_p2_mp3_h',
'p3'=>'http://lyd.nrk.no/nrk_radio_p3_mp3_h',
'p13'=>'http://lyd.nrk.no/nrk_radio_p13_mp3_h',
'p1pluss'=>'http://lyd.nrk.no/nrk_radio_p1pluss_mp3_h',
'jazz'=>'http://lyd.nrk.no/nrk_radio_jazz_mp3_h',
'klassisk'=>'http://lyd.nrk.no/nrk_radio_klassisk_mp3_h',
'nyheter'=>'http://lyd.nrk.no/nrk_radio_alltid_nyheter_mp3_h',
'mp3'=>'http://lyd.nrk.no/nrk_radio_mp3_mp3_h'
);

if(array_key_exists($ch,$chs)){
	`/usr/local/bin/radio.sh $chs[$ch]`;
}else{

}
if($_GET['off']=='Av'){
	`/usr/local/bin/radio.sh off`;	
}
?>

<html><head>Nettradio</head><body>
<form action="" method="get">
<select name="ch">
<option value="p1">NRK P1</option>
<option value="p2">NRK P2</option>
<option value="p3">NRK P3</option>
<option value="p13">NRK P13</option>
<option value="p1pluss">NRK P1+</option>
<option value="jazz">NRK alltid jazz</option>
<option value="klassisk">NRK alltid klassisk</option>
<option value="mp3">NRK mp3</option>
<option value="nyheter">NRK alltid nyheter</option>
</select>
<input type="submit" value="Velg" />
<input name="off" type="submit" value="Av" />
</form>
</body></html>

