
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

$(".disabled-tr select, .disabled-tr input, .disabled-tr textarea").prop("disabled", true);


/********************************************************************/
// SHOW PRODUCT IMAGE 
/********************************************************************/

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

/*
window.addEventListener('load', function() {
    document.querySelector('input[type="file"]').addEventListener('change', function() {

        // image extension validation
        if (!this.files[0].name.match(/.(jpg|jpeg|png|gif)$/i)){
            alert('Please select Image file ');
            $('#files').val("");
        }
        else {
            //  Image file size less then 1MB
            if(this.files[0].size > 1000000){
                alert('Image file size less then 1MB');
                $('#files').val("");

            }
            else if (this.files && this.files[0]) {
                var img = document.querySelector('img');  // $('img')[0]
                img.src = URL.createObjectURL(this.files[0]); // set src to blob url
                $(".close").show()
                
            }
        }
    });
  });
  $('.close').click(function (e) {
    $('img').attr('src', '');
    $('#files').val("");
    $('.close').hide()

    
});

*/
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
// bundle table -- Changes Made By Lawrence
/********************************************************************/
// Add Row
/*
var number = 1
function addRow() {
    number += 1
    $('#table').append('<tr id="row'+number+'"><th scope="row'+number+'">'+number+'</th><td> <select class="form-control" id="product_type'+number+'" name="product_type'+number+'" onclick="bundle('+number+')" style="width: 107% !important;"><option value="------">------</option><option value="Goods">GOODS</option><option value="Services">SERVICES</option></td><td><select class="form-control" id="Product_name'+number+'" name="Product_name'+number+'" style="margin-left: 31px !important;width: 142% !important;"><option value="product_name">------</option></td><td><input type="number" class="form-control" id="Quantity'+number+'" name="Quantity'+number+'" style="margin-left: 90px !important;width:37% !important;"></td><td><button class="btn btn-danger btn-remove" type="button" id="'+number+'" name="'+number+'" onclick="removeRow(number)" style="padding-left:7px;padding-right:7px;margin-top:-8px;padding-top:6px;padding-bottom:6px;width: 96%;"><b>X</b></button></td></tr>')
    
};
*/
var number = 1
function addRow() {
    number += 1
    htm = '<tr id="row_'+number+'"><th>'+number+'</th>';
    htm += '<td> <select class="form-control" name="prod_type[]" onchange="bundle($(this),'+number+')" style="width: 107% !important;"><option value="">------</option><option value="0">GOODS</option><option value="1">SERVICES</option></td>';
    htm += '<td><select class="form-control" id="product_name_'+number+'" name="prod_name[]" style="margin-left: 31px !important;width: 142% !important;"><option value="">------</option></td>';
    htm += '<td><input type="number" class="form-control" name="qty[]" style="margin-left: 90px !important;width:37% !important;"></td>';
    htm += '<td><button class="btn btn-danger btn-remove" type="button" onclick="removeRow('+number+')" style="padding-left:7px;padding-right:7px;margin-top:-8px;padding-top:6px;padding-bottom:6px;width: 96%;"><b>X</b></button></td></tr>';
    $('#table').append(htm);
    
};


function removeRow(a) {
    $('#row_'+a+'').remove();
    number -=1;
}

function bundle(elem, ids){
    if($(elem).val()!=""){
        $('tr#row_'+ids+' input').val("");
        get_products($(elem).val(), ids);        
    }else{
        $('tr#row_'+ids+' select').val("");
        $('tr#row_'+ids+' input').val("");
    }
}

function get_products(prod_type, ids){
    $.get("/prducts/bundle/",{'prod_type' : prod_type},function(data){
        $("select#product_name_"+ids).empty().append(data);
    });
}

/********************************************************************/
// bundle table   select INPUT FIELD
/********************************************************************/

/*
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
*/

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
        
        
    }
    else{
        $("#b_table").hide()
        $("#bundle_table").hide()
        $("#img_box").show()
        $("#hsn").show()
        $("#hsn_list").show()
        $("#img_file").show()
        $("#units").show()
       
    }
}

// COMMENTED BY LAWRENCE

/********************************************************************/
// ADD PRODUCT SALE ACCOUNT SELECT OPTION
/********************************************************************/
/*
    var opt = {
        Income:[
            {name:"Discount"},
            {name:"General Income"},
            {name:"Interest Income"},
            {name:"Late Fee Income"},
            {name:"Other Charges"},
            {name:"Sales"},
            {name:"Shipping Charges"},
        ],       
    };
    
    $(function(){
        var $select = $('#id_sales_account');
        $.each(opt, function(key, value){
            var group = $('<optgroup label="' + key + '" />').css('color','yello');
            $.each(value, function(){
                $('<option />').val(this.name).html(this.name).appendTo(group);
            });
            group.appendTo($select);
        });
    });
*/
/********************************************************************/
// INPUT TYPE NUMBER SROLL HIDE
/********************************************************************/

// Disable Mouse scrolling
$('input[type=number]').on('mousewheel',function(e){ $(this).blur(); });
// Disable keyboard scrolling
$('input[type=number]').on('keydown',function(e) {
    var key = e.charCode || e.keyCode;
    // Disable Up and Down Arrows on Keyboard
    if(key == 38 || key == 40 ) {
	e.preventDefault();
    } else {
	return;
    }
});

/*******************************************************************/
//  CODE BY LAWRENCE
/*******************************************************************/

function delete_bundle_product(ids, pro_id, sku, name){

    if(sku!="" && name!="") $("#product_details_span").text(sku +" - "+name);
    else if(sku!="" && name=="") $("#product_details_span").text(sku);
    else if(sku=="" && name!="") $("#product_details_span").text(name);
    else $("#product_details_span").text("");

    $("#product_delete_link").attr("href","/delete_bundle_product/"+ids+"/"+pro_id+"/"); 

    $("#delProductModal").modal('show');
}


function edit_bundle_product(ids, pro_id, sku, name, qty = 0){
    if(sku!="" && name!="") $("#product_edit_details_span").text(sku +" - "+name);
    else if(sku!="" && name=="") $("#product_edit_details_span").text(sku);
    else if(sku=="" && name!="") $("#product_edit_details_span").text(name);
    else $("#product_edit_details_span").text("");

    $("#product_edit_link").attr("href","/edit_bundle_product/"+ids+"/"+pro_id+"/"); 

    $("#bundle_product_quantity").val(qty);
    $("#bundle_product_obj").val(pro_id);
    
    $("#editProductModal").modal('show');
}
