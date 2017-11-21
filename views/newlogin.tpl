<!DOCTYPE html>
<html> 
  <head>
    <meta charset="utf-8">
    <title>Innskrá</title>
  </head>
  <body>
  <form method='post'>
      <h3>Nýskráningarform:</h3>
      Notendanafn:<br>
      <input type="text" name='user' required><br>
      Lykilorð verður að vera minsta kosti 6 stafir og 3 tölustafir :<br>
      <input type="text" name='pass' required pattern="^[a-z]{6}\d{3}"><br>
      <input type='submit' value='Innskrá'>
      <input type='reset' value='Hreinsa'>
  </form>    
  </body>
</html>