<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello Translation</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <input type="text" id="language_code" placeholder="Enter language code (e.g., es, fr, en)">
    <button id="btn_translate">Translate</button>
    <div id="hello"></div>

    <script>
        $(document).ready(function() {
            $("#btn_translate").on("click", function() {
                const languageCode = $("#language_code").val(); // Get the entered language code
                const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

                // Fetch the translation
                $.get(apiUrl, function(data) {
                    const translation = data.hello; // Extract the translated "Hello"
                    $("#hello").text(translation); // Display the translation in the DIV#hello
                }).fail(function() {
                    $("#hello").text("Translation not available for this language.");
                });
            });
        });
    </script>
</body>
</html>

