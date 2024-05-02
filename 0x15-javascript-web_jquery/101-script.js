<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My List</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <ul class="my_list">
        <!-- Existing list items (if any) -->
    </ul>

    <div id="add_item">Add Item</div>
    <div id="remove_item">Remove Last Item</div>
    <div id="clear_list">Clear List</div>

    <script>
        $(document).ready(function() {
            // Add item when clicking on DIV#add_item
            $("#add_item").on("click", function() {
                const newItem = "<li>Item</li>";
                $(".my_list").append(newItem);
            });

            // Remove last item when clicking on DIV#remove_item
            $("#remove_item").on("click", function() {
                $(".my_list li:last-child").remove();
            });

            // Clear the entire list when clicking on DIV#clear_list
            $("#clear_list").on("click", function() {
                $(".my_list").empty();
            });
        });
    </script>
</body>
</html>

