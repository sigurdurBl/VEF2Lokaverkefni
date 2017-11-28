<!DOCTYPE html>
<html> 
  <head>
    <meta charset="utf-8">
    <title>login</title>
  </head>
  <body>
  <form method='post' action='/doinnskra' accept-charset="ISO-8859-1">
      <h3>Innskráningarform:</h3>
      Notendanafn:<br>
      <input type="text" name='user' required><br>
      Lykilorð <br>
      <input type="text" name='pass' required><br>
      <input type='submit' value='Nýskrá'>
      <input type='reset' value='Hreinsa'>
  </form>    
  </body>
</html>