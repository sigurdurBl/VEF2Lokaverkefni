<!DOCTYPE html>
<html> 
  <head>
    <meta charset="utf-8">
    <title>Innskrá</title>
  </head>
  <body>
  <form method='post' action='/donyskra'>
      <h3>Nýskráningarform:</h3>
      Notendanafn:<br>
      <input type="text" name='user' required><br>
      Lykilorð verður að vera minsta kosti 8 stafir og 2 tölustafir :<br>
      <input type="text" name='pass' required><br>
      <input type='submit' value='Innskrá'>
      <input type='reset' value='Hreinsa'>
  </form>    
  </body>
</html>