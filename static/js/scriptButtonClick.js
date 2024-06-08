$("#uploadFile").click(function(e){
        e.preventDefault();
        var fileInput = document.getElementById('fileToUpload');
        var file = fileInput.files[0];
        // Check file type and size
        if(file.type != "application/json") {
            alert("Please upload a .json file");
            return;
        }
        if(file.size > 1048576) { // size in bytes
            alert("File size should not exceed 1MB");
            return;
        }
        
        var reader = new FileReader();
        reader.onload = function(e) {
            var contents = e.target.result;
            var jsonContents = JSON.parse(contents);
            console.log(jsonContents);
            $('#envUrl').val(jsonContents.base_url);
            $('#username').val(jsonContents.username);
            $('#password').val(jsonContents.password);
            $('#ompName').val(jsonContents.package_name);
        };
        reader.readAsText(file);
});

$("#createPackage").submit(function(e){
        e.preventDefault();
        var formData = new FormData();
        formData.append('base_url', $('#envUrl').val());
        formData.append('username', $('#username').val());
        formData.append('password', $('#password').val());
        formData.append('package_name', $('#ompName').val());
        if ($('#fileToUpload')[0].files.length > 0) { // Check if file is selected
            formData.append('file', $('#fileToUpload')[0].files[0]);
        }
        $.ajax({
            url: '/',
            type: 'post',
            data: formData,
            contentType: false,
            processData: false,
            
            beforeSend: function() {
                $('#loading-overlay').show();  // Show the overlay
            },
            complete: function() {
                $('#loading-overlay').hide();  // Hide the overlay
            },

            success: function(response){
                alert(JSON.stringify(response.message));
                console.log(response.message);  
            },
            error: function(error){
                alert('Error: ' + JSON.stringify(error));
            }
        });
});
