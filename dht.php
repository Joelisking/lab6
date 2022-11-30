<?php
$servername="localhost";
$username="root";
$password="";    
$dbname="lab6";

$Temp=$_GET['temp'];

// $LDRValue=$_GET['LDRValue'];
// $Temperature=$_GET['Temperature'];
$con = mysqli_connect($servername,$username,$password,$dbname);

$sql = "INSERT INTO dht (temp) VALUES ('{$Temp}')";

if (mysqli_query($con, $sql)){
echo "New record created successfully";
}
else{
    echo "Failed";
}

?>
