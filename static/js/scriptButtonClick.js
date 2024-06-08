$("#fileToUpload").change(function(e){
        //e.preventDefault();
        var fileInput = document.getElementById('fileToUpload');
        var file = fileInput.files[0];

        // Check if a file was selected
        if (!file) {
           
            return;  // Exit the function if no file was selected
        }

        // Check file type and size
        if(file.type != "application/json") {
            alert("Please upload a .json file");
            fileInput.value = "";  // Reset the file input field
            return;
        }
        if(file.size > 1048576) { // size in bytes
            alert("File size should not exceed 1MB");
            fileInput.value = "";  // Reset the file input field
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

$("#ompForm").submit(function(e){
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


$("#addToOmpButton").click(function(e){
    e.preventDefault();
    var formData = new FormData();
    formData.append('base_url', $('#envUrl').val());
    formData.append('username', $('#username').val());
    formData.append('password', $('#password').val());
    formData.append('package_name', $('#ompName').val());
    if ($('#objectsFile')[0].files.length > 0) { // Check if file is selected
        var file = $('#objectsFile')[0].files[0];
        var fileType = file.name.split('.').pop().toLowerCase();
        if (fileType !== 'xls' && fileType !== 'xlsx') {
            alert('Invalid file type. Please select a .xlsx or .xls file.');
            return;
        }
        formData.append('objects_file', file);
    }
    $.ajax({
        url: '/add_to_omp',
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

$("#clearFile").click(function(e){
    e.preventDefault();
    $('#objectsFile').val('');
     // Enable the 'Create OMP' button when the file input is cleared
     $('#createOMPbtn').prop('disabled', false);
});

$("#objectsFile").change(function(e){
    var fileInput = document.getElementById('objectsFile');
    var file = fileInput.files[0];

    // Check if a file was selected
    if (!file) {
        // Enable the 'Create OMP' button if no file was selected
        $('#createOMPbtn').prop('disabled', false);
        return;
    }
    // Check file type
    var fileType = file.name.split('.').pop().toLowerCase();
    if (fileType !== 'xls' && fileType !== 'xlsx') {
        alert('Invalid file type. Please select a .xlsx or .xls file.');
        fileInput.value = "";  // Reset the file input field
        return;
    }
     // Disable the 'Create OMP' button if an Excel file was selected
     $('#createOMPbtn').prop('disabled', true);
 });