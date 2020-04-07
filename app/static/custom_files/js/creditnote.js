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
$('#table').append('<tr id="row'+number+'"><th scope="row'+number+'">'+number+'</th><td><select class="form-control" id="ItemName'+number+'" name="ItemName'+number+'" style="width: 397%;"><option value="">------</option></td><td><input type="text" class="form-control" id="type'+number+'" name="type'+number+'" style="width: 88%;margin-left: 71%;"></td><td><input type="text" class="form-control" id="Price'+number+'" name="Price'+number+'" style="width: 86%;margin-left: 62%;"></td><td><input type="number" class="form-control" id="Quantity1'+number+'" name="Quantity1'+number+'" style="width: 88%;margin-left: 53%;"></td><td><input type="text" class="form-control" id="Discount'+number+'" name="Discount'+number+'" style="margin-left: 52%;width: 66%;"></td><td><input type="text" class="form-control" id="Tax'+number+'" name="Tax'+number+'" style="width: 66%;margin-left: 35%;"></td><td><input type="text" class="form-control" id="Amount'+number+'" name="Amount'+number+'"></td><td><button class="btn btn-danger btn-remove" type="button" id="'+number+'" name="'+number+'" onclick="removeRow(number)" style="width:96%;padding-left:7px;padding-right:7px;margin-top:-8px;padding-top:6px;padding-bottom: 6px;"><b>X</b></button></td></tr>')

};

function removeRow(a) {
// console.log("aaaaaaaaaaaa")
// var button_id = $(this).attr("id");
// console.log(button_id)
console.log(a)
$('#row'+a+'').remove();
number -=1
}

/************************************************************ */
// GET CONTACT/product DETAILS
/************************************************************ */

function data() {
    var contact = $('#customerName :selected').text();
    console.log(contact)
    $.ajax({
        type:"GET",
        url: "/creditnote/data/"+contact+"",
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

};
