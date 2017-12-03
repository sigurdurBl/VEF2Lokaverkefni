<!DOCTYPE html>
<html>
<head>
    <title>Vefverslun</title>
    <meta charset="utf-8">
</head>
<body>
<h2>Veldu vöru í körfu!</h2>

<div>
    % for i in range(len(products)):
    <button class="myButt one">
       <p> <a href="/cart/add/{{ products[i]["pid"] }}"> {{ products[i]["name"] }} </a> </p>
    </button>
    % end
</div>
<a href="/logout"> log out </a>

   
</body>
</html>