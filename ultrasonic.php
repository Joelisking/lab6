<?php
$servername="localhost";
$username="root";
$password="";    
$dbname="lab6";

$DistanceCm=$_GET['DistanceCm'];

// $LDRValue=$_GET['LDRValue'];
// $Temperature=$_GET['Temperature'];
$con = mysqli_connect($servername,$username,$password,$dbname);

$sql = "INSERT INTO ultrasonic (distance) VALUES ('{$DistanceCm}')";

if (mysqli_query($con, $sql)){
echo "New record created successfully";
}
else{
    echo "Failed";
}

?>