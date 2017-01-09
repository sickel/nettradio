<?php

$ch=$_GET['ch'];
// echo($ch);
echo('<br/>');
$chs=array(
'p1'=>array('NRK P1','http://lyd.nrk.no/nrk_radio_p1_ostlandssendingen_mp3_h'),
'p2'=>array('NRK P2','http://lyd.nrk.no/nrk_radio_p2_mp3_h'),
'p3'=>array('NRK P3','http://lyd.nrk.no/nrk_radio_p3_mp3_h'),
'p13'=>array('NRK P13','http://lyd.nrk.no/nrk_radio_p13_mp3_h'),
'p1pluss'=>array('NRK P1+','http://lyd.nrk.no/nrk_radio_p1pluss_mp3_h'),
'jazz'=>array('NRK alltid jazz','http://lyd.nrk.no/nrk_radio_jazz_mp3_h'),
'klassisk'=>array('NRK alltid klassisk','http://lyd.nrk.no/nrk_radio_klassisk_mp3_h'),
'nyheter'=>array('NRK alltid nyheter','http://lyd.nrk.no/nrk_radio_alltid_nyheter_mp3_h'),
'mp3'=>array('NRK mp3','http://lyd.nrk.no/nrk_radio_mp3_mp3_h')
);
$file='ch.txt';
if(array_key_exists($ch,$chs)){
  $stream=$chs[$ch][1];
  `/usr/local/bin/radio.sh $stream`;
  $f=fopen($file,"w");
  fwrite($f,$ch);
  fclose($f);
}else{
   $f=fopen($file,"r");
   if($f){
     $ch=fread($f,filesize($file));
     fclose($f);
   }
}
if($_GET['off']=='Av'){
	`/usr/local/bin/radio.sh off`;	
}
?>
<html><head><title>Nettradio</title></head><body>
<form action="" method="get">
<select name="ch">
<?php
foreach($chs as $k=>$v){
    $sel="";
    if($k==$ch){
        $sel="selected";
    }
    print("<option $sel value=\"{$k}\">{$v[0]}</option>\n");
}
?>
</select>
<input type="submit" value="Velg" />
<input name="off" type="submit" value="Av" />
</form>
</body></html>

