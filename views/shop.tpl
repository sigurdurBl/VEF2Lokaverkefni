<!DOCTYPE html>
<html>
<head>
    <title>Vefverslun</title>
    <meta charset="utf-8">
    <link href='/css/shop.css' rel='stylesheet' type='css'>
</head>
<body>
<h2>Veldu vöru í körfu!</h2>

<div class="myButt one">
    % for i in range(len(products)):
    <button class="">
    	<div class="insider"></div>
       <p> <a href="/cart/add/{{ products[i]["pid"] }}"> {{ products[i]["name"] }} </a> </p>
    </button>
    % end
</div>
<a href="/logout"> log out </a>

   
</body>
</html>