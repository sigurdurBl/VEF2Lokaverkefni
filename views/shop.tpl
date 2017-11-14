<!DOCTYPE html>
<html>
<head>
    <title>Vefverslun</title>
    <meta charset="utf-8">
    <link href='/static/styles.css' rel='stylesheet' type='css'>
</head>
<body>
<h2>Veldu vöru í körfu!</h2>
<div>
    % for i in range(len(products)):
       <p> <a href="/cart/add/{{ products[i]["pid"] }}"> {{ products[i]["name"] }} </a> </p>
    % end
</div>

   
</body>
</html>