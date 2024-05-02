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
            // Function to fetch and display the translation
            function fetchTranslation(languageCode) {
                const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

                $.get(apiUrl, function(data) {
                    const translation = data.hello; // Extract the translated "Hello"
                    $("#hello").text(translation); // Display the translation in the DIV#hello
                }).fail(function() {
                    $("#hello").text("Translation not available for this language.");
                });
            }

            // Fetch translation when clicking the button
            $("#btn_translate").on("click", function() {
                const languageCode = $("#language_code").val(); // Get the entered language code
                fetchTranslation(languageCode);
            });

            // Fetch translation when pressing ENTER in the input field
            $("#language_code").on("keypress", function(event) {
                if (event.key === "Enter") {
                    const languageCode = $("#language_code").val();
                    fetchTranslation(languageCode);
                }
            });
        });
    </script>
</body>
</html>

