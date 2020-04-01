
$("#id_is_sales").on("click", function(){
    if($(this).prop("checked") === true){
        $("#id_marked_price, #id_sales_account, #id_discount, #id_selling_price").prop("readonly", false);
    }else{
        $("#id_marked_price , #id_sales_account, #id_discount, #id_selling_price").prop("readonly", true);
    }
});


$("#id_is_purchase").on("click", function(){
    if($(this).prop("checked") === true){
        $("#id_cost_price, #id_purchase_account").prop("readonly", false);
    }else{
        $("#id_cost_price, #id_purchase_account").prop("readonly", true);
    }
});


/********************************************************************/
// SHOW PRODUCT IMAGE 
/********************************************************************/

        //I added event handler for the file upload control to access the files properties.
        document.addEventListener("DOMContentLoaded", init, false);

        //To save an array of attachments 
        var AttachmentArray = [];

        //counter for attachment array
        var arrCounter = 0;

        //to make sure the error message for number of files will be shown only one time.
        var filesCounterAlertStatus = false;

        //un ordered list to keep attachments thumbnails
        var ul = document.createElement('ul');
        ul.className = ("thumb-Images");
        ul.id = "imgList";

        function init() {
            //add javascript handlers for the file upload event
            document.querySelector('#files').addEventListener('change', handleFileSelect, false);
        }

        //the handler for file upload event
        function handleFileSelect(e) {
            //to make sure the user select file/files
            if (!e.target.files) return;

            //To obtaine a File reference
            var files = e.target.files;

            // Loop through the FileList and then to render image files as thumbnails.
            for (var i = 0, f; f = files[i]; i++) {

                //instantiate a FileReader object to read its contents into memory
                var fileReader = new FileReader();

                // Closure to capture the file information and apply validation.
                fileReader.onload = (function (readerEvt) {
                    return function (e) {
                        
                        //Apply the validation rules for attachments upload
                        ApplyFileValidationRules(readerEvt)

                        //Render attachments thumbnails.
                        RenderThumbnail(e, readerEvt);

                        //Fill the array of attachment
                        FillAttachmentArray(e, readerEvt)
                    };
                })(f);

                // Read in the image file as a data URL.
                // readAsDataURL: The result property will contain the file/blob's data encoded as a data URL.
                // More info about Data URI scheme https://en.wikipedia.org/wiki/Data_URI_scheme
                fileReader.readAsDataURL(f);
            }
            document.getElementById('files').addEventListener('change', handleFileSelect, false);
        }

        //To remove attachment once user click on x button
        jQuery(function ($) {
            $('div').on('click', '.img-wrap .close', function () {
                var id = $(this).closest('.img-wrap').find('img').data('id');

                //to remove the deleted item from array
                var elementPos = AttachmentArray.map(function (x) { return x.FileName; }).indexOf(id);
                if (elementPos !== -1) {
                    AttachmentArray.splice(elementPos, 1);
                }

                //to remove image tag
                $(this).parent().find('img').not().remove();

                //to remove div tag that contain the image
                $(this).parent().find('div').not().remove();

                //to remove div tag that contain caption name
                $(this).parent().parent().find('div').not().remove();

                //to remove li tag
                var lis = document.querySelectorAll('#imgList li');
                for (var i = 0; li = lis[i]; i++) {
                    if (li.innerHTML == "") {
                        li.parentNode.removeChild(li);
                    }
                }

            });
        }
        )

        //Apply the validation rules for attachments upload
        function ApplyFileValidationRules(readerEvt)
        {
            //To check file type according to upload conditions
            if (CheckFileType(readerEvt.type) == false) {
                alert("The file (" + readerEvt.name + ") does not match the upload conditions, You can only upload jpg/png/gif files");
                e.preventDefault();
                return;
            }

            //To check file Size according to upload conditions
            if (CheckFileSize(readerEvt.size) == false) {
                alert("The file (" + readerEvt.name + ") does not match the upload conditions, The maximum file size for uploads should not exceed 300 KB");
                e.preventDefault();
                return;
            }

            //To check files count according to upload conditions
            if (CheckFilesCount(AttachmentArray) == false) {
                if (!filesCounterAlertStatus) {
                    filesCounterAlertStatus = true;
                    alert("You have added more than 4 files. According to upload conditions you can upload 10 files maximum");
                }
                e.preventDefault();
                return;
            }
        }

        //To check file type according to upload conditions
        function CheckFileType(fileType) {
            if (fileType == "image/jpeg") {
                return true;
            }
            else if (fileType == "image/png") {
                return true;
            }
            else if (fileType == "image/gif") {
                return true;
            }
            else {
                return false;
            }
            return true;
        }

        //To check file Size according to upload conditions
        function CheckFileSize(fileSize) {
            if (fileSize < 300000) {
                return true;
            }
            else {
                return false;
            }
            return true;
        }

        //To check files count according to upload conditions
        function CheckFilesCount(AttachmentArray) {
            //Since AttachmentArray.length return the next available index in the array, 
            //I have used the loop to get the real length
            var len = 0;
            for (var i = 0; i < AttachmentArray.length; i++) {
                if (AttachmentArray[i] !== undefined) {
                    len++;
                }
            }
            //To check the length does not exceed 10 files maximum
            if (len > 3) {
                return false;
            }
            else
            {
                return true;
            }
        }

        //Render attachments thumbnails.
        function RenderThumbnail(e, readerEvt)
        {
            var li = document.createElement('li');
            ul.appendChild(li);
            li.innerHTML = ['<div class="img-wrap"> <span class="close">&times;</span>' +
                '<img class="thumb" src="', e.target.result, '" title="', escape(readerEvt.name), '" data-id="',
                readerEvt.name, '" />' + '</div>'].join('');

            var div = document.createElement('div');
            div.className = "FileNameCaptionStyle";
            li.appendChild(div);
            div.innerHTML = [readerEvt.name].join('');
            document.getElementById('Filelist').insertBefore(ul, null);
        }

        //Fill the array of attachment
        function FillAttachmentArray(e, readerEvt)
        {
            AttachmentArray[arrCounter] =
            {
                AttachmentType: 1,
                ObjectType: 1,
                FileName: readerEvt.name,
                FileDescription: "Attachment",
                NoteText: "",
                MimeType: readerEvt.type,
                Content: e.target.result.split("base64,")[1],
                FileSizeInBytes: readerEvt.size,
            };
            arrCounter = arrCounter + 1;
        }
// $(document).ready(function() {
//     if (window.File && window.FileList && window.FileReader) {
//       $("#files").on("change", function(e) {
//         var files = e.target.files,
//           filesLength = files.length;
//           console.log(files)
//           console.log(filesLength)
//           var check = 1
          
//         for (var i = 0; i < filesLength; i++) {
//           var f = files[i]
//           console.log(i)
//           var fileReader = new FileReader();
//            fileReader.onload = (function(e) {
//             var file = e.target;
//             $("<span class=\"pip\">" +
//               "<img class=\"imageThumb\" src=\"" + e.target.result + "\" title=\"" + file.name + "\"/>" +
//               "<br/><span class=\"remove\">Remove image</span>" +
//               "</span>").insertAfter("#files");
//             $(".remove").click(function(){
//               $(this).parent(".pip").remove();
//             });
            
//             // Old code here
//             /*$("<img></img>", {
//               class: "imageThumb",
//               src: e.target.result,
//               title: file.name + " | Click to remove"
//             }).insertAfter("#files").click(function(){$(this).remove();});*/
            
//           });
//           fileReader.readAsDataURL(f);
//         }
      
//       });
    
//     } else {
//       alert("Your browser doesn't support to File API")
//     }
//   });
// window.addEventListener('load', function() {
//     document.querySelector('input[type="file"]').addEventListener('change', function() {
//         if (this.files && this.files[0]) {
//             var img = document.querySelector('img');  // $('img')[0]
//             img.src = URL.createObjectURL(this.files[0]); // set src to blob url
            
//         }
//     });
//   });
  

/********************************************************************/
// view product active inactive and delete 
/********************************************************************/



function status(a,b) {

    var status = 's'+a.toString()
    var c = document.getElementById(status).innerHTML;
    console.log(c.length)
    if(c.length == 13){
        $.ajax({
        type: 'GET',
        url: "/products/status_change/deactivate/"+a+"",
        success: function() {
            document.getElementById(a).innerHTML = 'clear'
            document.getElementById(status).innerHTML = 'Make Active'
            $('#'+'status'+a.toString()).modal('hide')
            document.getElementById('text').innerHTML = 'Are you sure you want to make '+b+' active '
            
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("some error");
        }

    });
    }
    if(c.length == 11){
        $.ajax({
        type: 'GET',
        url: "/products/status_change/activate/"+a+"",
        success: function() {
            document.getElementById(a).innerHTML = 'check'
            document.getElementById(status).innerHTML = 'Make Inactive'
            $('#'+'status'+a.toString()).modal('hide')
            document.getElementById('text').innerHTML = 'Are you sure you want to make '+b+' inactive '
            
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("some error");
        }

    });
    }    
}
function nodeactive(d) {
$('#'+'status'+d.toString()).modal('hide')
}
function noactive(d) {
$('#'+'status'+d.toString()).modal('hide')
}

// //////////////////////////////////////////////////
// delete and cancel
function remove(c) {
console.log(c)
var remove = 't'+c
console.log(remove)
$.ajax({
        type: 'GET',
        url: "/products/delete/"+c+"",
        success: function() {
            console.log('xxxxxxxx')
            $("#"+remove).hide();
            $('#'+'del'+c.toString()).modal('hide')
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("some error");
        }

    });
}

function can(d) {
$('#'+'del'+d.toString()).modal('hide')
}



/********************************************************************/
// bundle table 
/********************************************************************/
// Add Row
var number = 1
function addRow() {
    number += 1
    $('#table').append('<tr id="row'+number+'"><th scope="row'+number+'">'+number+'</th><td> <select class="form-control" id="product_type'+number+'" name="product_type'+number+'" onclick="bundle('+number+')" style="width: 107% !important;"><option value="------">------</option><option value="Goods">GOODS</option><option value="Services">SERVICES</option></td><td><select class="form-control" id="Product_name'+number+'" name="Product_name'+number+'" style="margin-left: 31px !important;width: 142% !important;"><option value="product_name">------</option></td><td><input type="number" class="form-control" id="Quantity'+number+'" name="Quantity'+number+'" style="margin-left: 90px !important;width:37% !important;"></td><td><button class="btn btn-danger btn-remove" type="button" id="'+number+'" name="'+number+'" onclick="removeRow(number)" style="padding-left:7px;padding-right:7px;margin-top:-8px;padding-top:6px;padding-bottom:6px;width: 96%;"><b>X</b></button></td></tr>')
    
};

function removeRow(a) {
    console.log(a)
    $('#row'+a+'').remove();
    number -=1
}

/********************************************************************/
// bundle table 
/********************************************************************/

    function bundle(number) {
        var value = $('#product_type'+number+' :selected').text();
        if(value == 'GOODS' || value == 'SERVICES'){
            $.ajax({
                type:"GET",
                url: "/prducts/bundle/"+value+"",
                dataType: "json",
                success: function(data){
                    var option = data.products
                    // CLEAN SELECT OPTION //
                    var select = document.getElementById('Product_name'+number+'');
                    var length = select.options.length;
                    for (i = length-1; i >= 1; i--) {
                        select.options[i] = null;
                    }
                    // END //

                    // ADD SELECT OPTION //
                    for(var i = 0;i < option.length;i++){
                        console.log(i)
                        $('<option/>').val(option[i]).html(option[i]).appendTo('#Product_name'+number+'');
                    }
                    // END //
                },
                error: function (rs, e) {
                    alert('Sorry, try again.');
                }
            });
        }
      }
    
/********************************************************************/
// product type to show and hide 
/********************************************************************/

function show_bundle(elem){
    var a = $('#id_product_type :selected').text();
    if(a == "BUNDLE"){
        $("#b_table").show()
        $("#bundle_table").show()
        $("#img_box").hide()
        $("#hsn").hide()
        $("#hsn_list").hide()
        $("#img_file").hide()
        $("#units").hide()
        $("#product").css("margin-top", "1.3%")
        
    }
    else{
        $("#b_table").hide()
        $("#bundle_table").hide()
        $("#img_box").show()
        $("#hsn").show()
        $("#hsn_list").show()
        $("#img_file").show()
        $("#units").show()
        $("#product").css("margin-top", "-18%")
    }
}



