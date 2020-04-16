$(document).ready(function(){
    $("#email").keydown(function(){
        var mail =  document.getElementById("email").value
        var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        console.log(mail)
        if(mail.match(mailformat)){
            // $("#mailValidation").val("Valid Email Address*");
            document.getElementById("mailValidation").innerHTML = "Valid Email Address*";
        }
        else{

            // $("#mailValidation").val("Invalide Email Address*");
            document.getElementById("mailValidation").innerHTML = "Invalide Email Address*";
           
        }
 
    });
});

//  date function
var d = new Date();
var day = d.getDate()
var month =  (d.getMonth() + 1).toString()
var year = d.getFullYear().toString()
if(day < 10 ){
    day = "0" + day.toString()
}
if(month.length < 2){
    month = "0" + month
}
var date = year+ '-' + month + '-' + day.toString()
$("#CreditNoteDate").val(date)
// ////////////////////////////////////////////////

// Add Row
var number = 1
function addRow() {
number += 1
$('#table').append('<tr id="row'+number+'" style="border:1px solid white;"><td scope="row'+number+'" style="border:1px solid white;">'+number+'</td><td style="border:1px solid white;"><select class="form-control select" id="ItemName'+number+'" name="ItemName'+number+'" onchange=product('+number+') style="padding-left:0px"><option value="-------">-------</option></select><input type="text" class="form-control" id="desc'+number+'" placeholder="Product Describtion" style="margin-top:1px;font-size: x-small;display: none;"></td><td style="border:1px solid white;"><input type="text" class="form-control" id="type'+number+'" name="type'+number+'" readonly></td><td style="border:1px solid white;"><input type="text" class="form-control" onkeypress="return restrictAlphabets(event)" onkeyup="calculate('+number+')" id="Price'+number+'" name="Price'+number+'"></td><td style="border:1px solid white;"><select class="form-control"  id="Unit'+number+'" name="Unit'+number+'" style="padding-left:0px;"><option value="-------">-------</option></select></td><td style="border:1px solid white;"><input type="number" class="form-control" id="Quantity'+number+'" onkeyup="calculate('+number+')" name="Quantity'+number+'"></td><td style="border:1px solid white;"><input type="text" class="form-control" onkeypress="return restrictAlphabets(event)" onkeyup="calculate('+number+')" id="Discount'+number+'" name="Discount'+number+'"><select class="form-control"  id="Dis'+number+'" name="Dis'+number+'" style="    background-color: white;color: black;position: absolute;padding-left: 0px;margin-top: -20px;width: 2%;margin-left: 71px;"><option value="%">%</option><option value="₹">₹</option></select></td><td style="border:1px solid white;"><font style="position: absolute;margin-left: 5%;color: white;margin-top: -1%;">%</font><input list="tax" class="form-control tax" maxlength="5" size="5"  onkeypress="return restrictAlphabets(event)" name="tax'+number+'" id="tax'+number+' style="padding: 12px 3px;padding-top: 6%;;width: 95%;margin-left: -5%;"><datalist id="tax"><option value="0"><option value="5"><option value="12"><option value="18"><option value="28"></datalist></td><td style="border:1px solid white;"><input type="text" class="form-control" onkeypress="return restrictAlphabets(event)" id="Amount'+number+'" name="Amount'+number+'" readonly></td><td style="border:1px solid white;"><button class="btn btn-danger btn-sm" type="button" id="'+number+'" name="'+number+'" onclick="removeRow(number)" style="margin-top: -4px;margin-bottom: -3px;width:95%"><b>X</b></button></td></tr>')

$(function () {
    $(".select").select2();
  });

$.ajax({
    type:"GET",
    url: "/creditnotes/add/"+1+"",
    dataType: "json",
    success: function(data){
        console.log(data.products)
        var option = data.products
        var unit = data.unit
        var id = data.ids
        for(var i = 0;i < option.length;i++){
            $('<option/>').val(id[i]).html(option[i]).appendTo('#ItemName'+number+'');
        }

        for(var i = 0;i < unit.length;i++){
            $('<option/>').val(unit[i]).html(unit[i]).appendTo('#Unit'+number+'');
        }
    },
    error: function (rs, e) {
        alert('Sorry, try again.');
    }
});

};

function removeRow(a) {
console.log(a)
$('#row'+a+'').remove();
number -=1
}


/************************************************************ */
// GET CONTACT DETAILS
/************************************************************ */

function data() {
    var contact = $('#customerName option').filter(':selected').val()
    //  $('#customerName :selected').text();
    console.log(contact)
    $.ajax({
        type:"GET",
        url: "/creditnote/contact/"+contact+"",
        dataType: "json",
        success: function(data){
            console.log(data.contacts)
            console.log(data.address)
            $("#email").val(data.contacts)
            var option = data.address
            // CLEAN SELECT OPTION //
            // var select = document.getElementById('BillingAddress1');
            // var length = select.options.length;
            // for (i = length-1; i >= 1; i--) {
            //     select.options[i] = null;
            // }
            // END //

            // ADD SELECT OPTION //
            for(var i = 0;i < option.length;i++){
                $('<option/>').val(option[i]).html(option[i]).appendTo('#BillingAddress');
            }
            // END //
        },
        error: function (rs, e) {
            alert('Sorry, try again.');
        }
    });

};

/************************************************************ */
// FETCH PRODUCT type/unit/price/product description
/************************************************************ */
function product(a) {
    var product = $('#ItemName'+a+' option').filter(':selected').val()
    //  $('#customerName :selected').text();
    if(product != "-------"){
        $.ajax({
            type:"GET",
            url: "/creditnote/product/"+product+"",
            dataType: "json",
            success: function(data){
                $("#desc"+a+"").show()
                $("#desc"+a+"").val(data.desc)
                if(data.product == 0){
                    $("#type"+a+"").val("GOODS")
                }
                else if(data.product == 1){
                    $("#type"+a+"").val("SERVICES")
                }
                else{
                    $("#type"+a+"").val("BUNDLE")
                }
                $("#Price"+a+"").val(data.price)
    
                $("#Unit"+a+"").val(data.unit)
                
            },
            error: function (rs, e) {
                alert('Sorry, try again.');
            }
        });
    }
    else{
        $("#desc"+a+"").hide()
        $("#desc"+a+"").val("")
        $("#type"+a+"").val("")
        $("#Price"+a+"").val("")
        $("#Unit"+a+"").val("")
    }
   
};

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
/*code: 48-57 Numbers 8  - Backspace, 35 - home key, 36 - End key 37-40: Arrow keys, 46 - Delete key*/
    function restrictAlphabets(e){
		var x=e.which||e.keycode;
		if((x>=48 && x<=57) || x==8 ||
			(x>=35 && x<=40)|| x==46)
			return true;
		else
			return false;
   }

/********************************************************************/
//  SHOW AND HIDE EMAIL CC
/********************************************************************/

// SHOW EMAIL CC
function show_cc_mail() {
    $(".ccemail").show()
    $("#close").show()
    $(".cc").css("margin-top","-3%")
  }

// HIDE EMAIL CC
function hide_cc_mail() {
    $(".ccemail").hide()
    $("#close").hide()
    $(".cc").css("margin-top","0px")
  }

/********************************************************************/
//  SHOW AND HIDE table
/********************************************************************/
  function hide_table() {
   var a = $('#checked').val()
   console.log(a)
    if ($('#checked').is(":checked")){
        $(".tbl").hide()
    }
    else{
        $(".tbl").show()
    }
  }

/********************************************************************/
// CELAN ATTACHEMENT
/********************************************************************/
function clean(){
    $("#Attachment").val('')
}

/********************************************************************/
// SEARCH INSIDE SELECT TAG
/********************************************************************/

$(document).ready(function() {
    // $('.mdb-select').materialSelect();
    $(function () {
        $(".select").select2();
      });
    });

/********************************************************************/
// product table validation
/********************************************************************/
// function error(){
//     // var price = $("#Price1").val()
//     // console.log(price)
//     // // showNotification('top','center')
//     // return false
//     for(var i = 1;i <= number;i++){
//         var product_type =  $("#type"+i+"").val()
//         if( product_type != null){
//             var price = $("#Price"+i+"").val()
//             var unit = $("#Unit"+i+"").val()
//             var quantity = $("#Quantity"+i+"").val()
//             if(price == ''){
//                 // alter("Fille Product table Proper")
//                 return false
//             }
//             else if(unit == '' || unit == '-------'){
//                 alter("Fille Product table Proper")
//                 return false
//             }
//             else if(quantity = ''){
//                 alter("Fille Product table Proper")
//                 return false
//             }

//         }
        
//     }
// }
/********************************************************************/
// CALCULATION
/********************************************************************/

function calculate(a){
    var price = $("#Price"+a+"").val();
    var quantity = $("#Quantity"+a+"").val();
    var discount = $("#Discount"+a+"").val();
    var dis_type = $("#Dis"+a+"").val();
    if(quantity != '' & quantity != '0'){
        var val = parseFloat(price) * parseInt(quantity)
        if(dis_type == '%'){
            if(discount == '' || discount == '0' || discount == '0.0'){
                if(price == '' || price == '0.0'){
                    $("#Amount"+a+"").val('')
                }else{
                    $("#Amount"+a+"").val(parseFloat(val))
                    sub_total()
                }   
            }
            else{
                var cal = (parseFloat(val) - (parseFloat(val) * (parseFloat(discount) / 100))).toFixed(2);
                if(price == '' || price == '0.0'){
                    $("#Amount"+a+"").val('')
                }else{
                    $("#Amount"+a+"").val(parseFloat(cal))
                    sub_total()
                }
            }
        }
        else if(dis_type == '₹'){
            if(discount == '' || discount == '0' || discount == '0.0'){
                if(price == '' || price == '0.0'){
                    $("#Amount"+a+"").val('')
                }else{
                    $("#Amount"+a+"").val(parseFloat(val))
                    sub_total()
                }   
            }
            else{
                var cal = (parseFloat(val) - parseFloat(discount)).toFixed(2);
                if(price == '' || price == '0.0'){
                    $("#Amount"+a+"").val('')
                }else{
                    $("#Amount"+a+"").val(parseFloat(cal))
                    sub_total()
                }
            }
            
           
        }
        
    }	
    else{
        $("#Amount"+a+"").val('')
    }
}

function dicount_type(a){
    calculate(a)
}

function sub_total(){
    var sub_total = 0
    for(var i=1; i <= number; i++){
        var a = $("#Amount"+i+"").val()
        sub_total +=  parseFloat(a)
    }
    $("#SubTotal").val(sub_total)
}