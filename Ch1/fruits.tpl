<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Fruits</title>
  </head>
  <body>
    <h1>Hello {{name}}</h1>
    <ul>
      %for fruit in fruits:
      <li><h3>{{fruit}}</h3></li>
      %end
    </ul>
    <form class="fruits" action="/favorite" method="post">
      What is your favorite fruit?
      <input type="text" name="fruit" value=""><br>
      <input type="submit" value="submit">
    </form>
  </body>
</html>
