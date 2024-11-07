<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome Page</title>
    
    <!-- MDL Inclusions -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
    <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
</head>

<body style="padding: 20px;">

    <?php
    $myVariable = "";
    if (isset($_POST['myVariable'])) {
        $myVariable = htmlspecialchars($_POST['myVariable']); // Sanitize input
    }
    ?>

    <h1 class="mdl-typography--display-2">My Program</h1>
    <p class="mdl-typography--body-1">My Variable is = <?php echo $myVariable; ?></p>

    <!-- Form to Update My Variable -->
    <form action="" method="POST" style="margin-top: 20px;">
        <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
            <input class="mdl-textfield__input" type="text" id="myVariable" name="myVariable">
            <label class="mdl-textfield__label" for="myVariable">Enter a Value</label>
        </div>
        
        <button class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored" type="submit">
            Submit
        </button>
    </form>

</body>
</html>
