<html>
    <head>
        <meta http-equiv="refresh" content="5">
    </head> 
<body> 
<?php

$websites = array("http://classification.40314604.qpc.hal.davecutting.uk/", "http://totalmarks.40314604.qpc.hal.davecutting.uk/",
 "http://maxmin.40314604.qpc.hal.davecutting.uk/","http://sortmodules.40314604.qpc.hal.davecutting.uk/");


echo "<h1>Student Grade Checker Dashboard</h>\n\n";
echo "<h2>Site Status at  ".gmdate("h:i:s")."(GMT)"."</h2>\n\n";

foreach ($websites as $url){
    unset($result);
    unset($status);
    unset($time);


//$data = file_get_contents($url);
$params = 'input_text=input_text=ll,55newlinepp,66';
$newurl = $url . '?' . $params;
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $newurl);
//curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
$headers = array ('Access-Control-Allow-Origin: *', 'Content-type: application/json');
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
$starttime = microtime(true);
$data = curl_exec($ch);
json_encode($data);
$stoptime =microtime(true);

if(curl_errno($ch)){
    $errormessage =curl_error($ch);
}
    if (isset($errormessage)){
        $status ='';
    echo "<br>"."<strong>"."Address: ".$url."</strong>"."<br>";
        //$status= "Website is down";
        echo "<br>"."Website status : Server is down"."<br>";
        echo "------------------------------------------------------------------------------------------------------------------------"."<br><br>";
    }else{
        $status =''; 
        echo "<strong>Address: ".$url ."</strong>"."<br>";
        $time = ($stoptime - $starttime) * 1000 ;
        $Status = "Server is up and running"."<br>";
        echo "Website status : ".$Status."Server response time (milliseconds): ".floor($time)."<br>";
        echo "Returned query information : " .$data."<br>";
        echo "-----------------------------------------------------------------------------------------------------------------------"."<br><br>";
        
        
    }
   
}

?>
