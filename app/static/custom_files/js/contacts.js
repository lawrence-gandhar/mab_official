/************************************************************ */
// code by Lawrence - Start
/************************************************************ */

$(document).ready(function(){
    setLocalStorageValue('form_errors_email', false);
    setLocalStorageValue('form_errors_phone', false);
    setLocalStorageValue('form_errors_pan', false);
    setLocalStorageValue('form_errors_gst', false);
    setLocalStorageValue('form_errors_url', false);
    setLocalStorageValue('form_errors_ifsc', false);
});

$("#app_id_input_2").removeClass("show-row").addClass("hide-row");

$("#more_address_table").find("input").attr('disabled', "true");
$("#more_address_table").find("select").attr('disabled', "true");

$("#tr-id_user_address_details_set-tr-0 td:nth-child(2)").find("table > tbody tr:nth-child(1)").hide();

$("#tr-id_user_address_details_set-tr-0 td:nth-child(2)").find("table > tbody tr:nth-child(1)").after(
    '<tr><td colspan="2" style="display:block; height:34px;"></td></tr>'
);

$("tr#tr-id_user_address_details_set-tr-0 > td:nth-child(2)").hide()
$(".is_billing_address, .is_shipping_address").prop("required",false);


function set_shipping(elem,ids){
    value = "False";
    if($(elem).prop("checked")) value = "True";
    $("select#id_user_address_details_set-"+(ids-1)+"-is_shipping_address").val(value);
}

function set_billing_diff(elem,ids){

    ids = ids - 1;

    value = "False";
    if($(elem).prop("checked")) value = "True";
    $("select#id_user_address_details_set-"+ids+"-is_billing_address_diff").val(value);
    $("select#id_user_address_details_set-"+(parseInt(ids)+1)+"-is_shipping_address").val(value);

    if(ids == 0){
        elem_htm = $("tr#tr-id_user_address_details_set-tr-0 > td:nth-child(2)");
    }else{
        ids = parseInt(ids)-2;
        elem_htm = $("tr#tr-id_user_address_details_set-tr-"+ids+" > td:nth-child(2)");
    }

    if($(elem).prop("checked") == true){
        $(elem_htm).show();
    }else{
        $(elem_htm).hide();
    }
}



/**************************************************************/
// Email Validation
/**************************************************************/

function valid_Email(elem){
    ret = validate_Email($(elem));
    if(!ret[0]){
        setLocalStorageValue('form_errors_email', true);
        $("#email_error").html(ret[1]);        
        $(elem).focus();
        $(".save_button, #editContactModal > .save_button").prop("disabled",true);
    }else{
        setLocalStorageValue('form_errors_email', false);
        $("#email_error").html("");
        $(".save_button, #editContactModal > .save_button").prop("disabled",false);
    } 
}


/**************************************************************/
// Phone/Mobile Validation
/**************************************************************/

function valid_Phone(elem){
    ret = validate_Phone($(elem));
    if(!ret[0]){
        setLocalStorageValue('form_errors_phone', true);
        $("#phone_error").html(ret[1]);
        $(elem).focus();
        $(".save_button, #editContactModal > .save_button").prop("disabled",true);
    }else{
        setLocalStorageValue('form_errors_phone', false);
        $("#phone_error").html("");
        $(".save_button, #editContactModal > .save_button").prop("disabled",false);
    } 
}


/**************************************************************/
// PAN Validation
/**************************************************************/

function valid_PAN(elem){
    ret = validate_PAN($(elem));
    if(!ret[0]){
        setLocalStorageValue('form_errors_pan', true);
        $("#pan_error").html("*Please enter valid pan card number");
        $(elem).focus();
        $(".save_button, #editContactModal > .save_button").prop("disabled",true);
    }else{
        setLocalStorageValue('form_errors_pan', false);
        $("#pan_error").html("");
        $(".save_button, #editContactModal > .save_button").prop("disabled",false);
    } 
}


/**************************************************************/
// GST Validation
/**************************************************************/

function valid_GST(elem){
    ret = validate_GST($(elem));
    if(!ret[0]){
        setLocalStorageValue('form_errors_get', true);
        $("#gst_error").html(ret[1]);
        $(elem).focus();
        $(".save_button, #editContactModal > .save_button").prop("disabled",true);
    }else{
        setLocalStorageValue('form_errors_get', false);
        $("#gst_error").html("");
        $(".save_button, #editContactModal > .save_button").prop("disabled",false);
    }  
}

/**************************************************************/
// WEBSITE Validation
/**************************************************************/

function valid_URL(elem){
    ret = validate_URL($(elem));
    if(!ret[0]){
        setLocalStorageValue('form_errors_url', true);
        console.log(elem.toString())
        $("#website_error").html(ret[1]);
        $(elem).focus();
        $(".save_button, #editContactModal > .save_button").prop("disabled",true);
    }else{
        setLocalStorageValue('form_errors_url', false);
        $("#website_error").html("");
        $(elem).css({"background-color":"transparent"});
        $(".save_button, #editContactModal > .save_button").prop("disabled",false);
    }  
}



/************************************************************ */
// IFSC Validations
/************************************************************ */

function valid_IFSC(elem){
    ret = validate_IFSC($(elem));
    if(!ret[0]){
        setLocalStorageValue('form_errors_ifsc', true);
        $("#ifcs_error").html(ret[1]);
        $(elem).focus();
        $(".save_button, #editContactModal > .save_button").prop("disabled",true);
    }else{
        setLocalStorageValue('form_errors_ifsc', false);
        $("#ifcs_error").html("");
        $(elem).css({"background-color":"transparent"});        
        $(".save_button, #editContactModal > .save_button").prop("disabled",false);
    }  
}

/************************************************************ */
// Check if APP ID exists
/************************************************************ */
function has_app_id(elem){

    $("#app_id_input").find("input").val("").removeClass("wrong_input");
    $("#id_app_id_check").empty();

    if($(elem).prop("checked") == true){
        $("#app_id_input").removeClass("hide-row").addClass("show-row");
    }
    else if($(elem).prop("checked") == false){
        $("#app_id_input").removeClass("show-row").addClass("hide-row");
        $("#app_id_input_2").removeClass("show-row").addClass("hide-row");
    }
}

//******************************************* 
//  CHECK IF APPLICATION ID EXISTS 
//********************************************

function check_app_id(elem){

    csrf = $("form").find("input[name='csrfmiddlewaretoken']").val();

    if($(elem).val()!=""){
        $("#wait_Modal").show();
        $("#wait_Modal").find("#loader_container").show();
        $("#wait_Modal").find("#modal-text").empty();

        $.post('/contacts/check_appid/',{'id':$(elem).val(), 'csrfmiddlewaretoken':csrf}, function(data){

            data = JSON.parse(data);

            if(data.ret == 0){ 
                
                $("#wait_Modal").find("#modal-text").html('<span style="color:#FF0000; font-weight:bold">Invalid Application ID</span>');              
                $("#id_app_id_check").empty().append('<i class="material-icons">clear</i>');
                $("#app_id_input_2").removeClass("show-row").addClass("hide-row");
                $("#success_svg").hide();
                $("#failure_svg").show().css("display", "block");
                $(elem).addClass("wrong_input");
            }
            if(data.ret =='1'){
                $("#id_app_id_check").empty().append('<i class="material-icons">check</i>');
                $("#wait_Modal").find("#modal-text").html('<span style="color:#00cc00; font-weight:bold">Found Application ID</span>');              
                $("#app_id_input_2").removeClass("hide-row").addClass("show-row");
                $("#failure_svg").hide();
                $("#success_svg").show().css("display", "block");
                $("#id_imported_user").val(data.id);
                $(elem).removeClass("wrong_input");
            }

            $("#svg_container").show();
            $("#wait_Modal").find(".modal-title").empty().text("Result");
            $("#wait_Modal").find("#loader_container").hide();
        });
    }
}

//******************************************* 
//  Check imported User
//********************************************

$("#id_is_imported_user").on("click", function(){

    if($(this).prop("checked") === true){

        csrf = $("form").find("input[name='csrfmiddlewaretoken']").val();

        $.post('/contacts/user_exists_in_list/',{'id':$("#id_imported_user").val(), 'csrfmiddlewaretoken':csrf}, function(data){
                        
            if(data == 0){
                r = confirm("Do you want to use the existing details of this user as the contact details");
                if (r === true) {
                    $("#id_contact_name").val('Existing App User');
                }else{
                    $(this).prop("checked", false);
                }
            }
            if(data >=1){
                r = confirm("A user with the same AppId exists in your contact list. Do you still want to create a new contact?");
                if (r === true) {
                    $("#id_contact_name").val('Existing App User');
                }else{
                    $(this).prop("checked", false);
                }
            }
        });
    }
});

/****************************************************************/
// Add Accounts Block
/****************************************************************/

$("#add_more_accounts").on("click", function(){
    inc = $("#id_form-TOTAL_FORMS").val();

    htm_all = '<tr class="tr-set-'+inc+'">';
    htm_all += '<td style="padding-top:10px; color:#FF0000; border:0px; border-bottom:3px solid #ccc;" colspan="2">';
    htm_all += '<i class="material-icons pull-right" style="cursor:pointer;" onclick="delete_account_block($(this),'+(parseInt(inc)-1)+')">delete_forever</i></td></tr>';

    $("#accounts-form tr.accounts_formset ").each(function(index, tr){

        xx = $(tr).html().replace("form-0", "form-"+inc)

        htm = '<tr class="tr-set-'+inc+'">'+xx+'</tr>';
        htm_all += htm;
    });

    $("#id_form-TOTAL_FORMS").val(parseInt(inc)+1);

    $("#accounts-form > table > tbody").append(htm_all);

});



/****************************************************************/
// Add Address Block
/****************************************************************/

$("#add_more_addresses").on("click",function(){

    inc = $("#id_user_address_details_set-TOTAL_FORMS").val();

    htm_all = '';

    htm = $("tr#tr-id_user_address_details_set-tr-0").html();

    htm_all = '<tr>';
    htm_all += '<td style="padding-top:10px; color:#FF0000; border:0px; border-bottom:3px solid #ccc;" colspan="2">';
    htm_all += '<i class="material-icons pull-right" style="cursor:pointer;" onclick="delete_address_block($(this),'+(parseInt(inc)-1)+')">delete_forever</i></td></tr>';
    htm_all += '<tr id="tr-id_user_address_details_set-tr-'+(parseInt(inc)-1)+'">'+htm+'</tr>';

    ids = parseInt(inc) + 1;
    row_num = 0;
    
    htm_all = htm_all.replace(/user_address_details_set-0/g, "user_address_details_set-"+ids);
    htm_all = htm_all.replace(/user_address_details_set-1/g, "user_address_details_set-"+parseInt(ids + 1));
    
    $("#address_table > tbody").append(htm_all);

    $("#tr-id_user_address_details_set-tr-"+(parseInt(inc)-1)+" td:nth-child(2)").find("table > tbody tr:nth-child(1)").hide();

    $("#id_user_address_details_set-TOTAL_FORMS").val(parseInt(inc) + 2);

    $("#tr-id_user_address_details_set-tr-"+(parseInt(inc)-1)+" td:nth-child(2)").find($(".address_is_billing_diff")).attr("onclick","set_billing_diff($(this),"+parseInt(ids + 1)+")")

});



/****************************************************************/
// Remove Address Block
/****************************************************************/

function delete_address_block(elem, ids){
    inc = $("#id_user_address_details_set-TOTAL_FORMS").val();
    $(elem).closest('tr').remove();
    $("#tr-id_user_address_details_set-tr-"+ids).remove();
    $("#id_user_address_details_set-TOTAL_FORMS").val(parseInt(inc) -2);
}

/****************************************************************/
// Remove Accounts Block
/****************************************************************/

function delete_account_block(elem, ids){
    inc = $("#id_user_address_details_set-TOTAL_FORMS").val();
    
    elem = $(elem).closest("tr").attr("class");

    $("tr."+elem).remove();
    $("#id_form-TOTAL_FORMS").val(parseInt(inc)-1);
}


$(".disabled-tr").find("input").attr("disabled","true");
$(".disabled-tr").find("select").attr("disabled","true");
$(".disabled-tr").find("textarea").attr("disabled","true");

$(".set_required").find("input").attr("required", "true");
$(".set_required").find("select").attr("required", "true");

$("#editAccountsModal").find("input").attr("required", "true");


/********************************************************************/
// Billing Clicked
/********************************************************************/

function billing_clicked(elem){

    var ids = $(elem).attr("id");

    ids = ids.replace("id_user_address_details_set-", "").replace("-is_billing_address_diff", "");

    if(ids == 0){
        elem_htm = $("tr#tr-id_user_address_details_set-tr-0 > td:nth-child(2)");
    }else{
        ids = parseInt(ids)-2;
        elem_htm = $("tr#tr-id_user_address_details_set-tr-"+ids+" > td:nth-child(2)");
    }

    if($(elem).prop("checked") == true){
        $(elem_htm).show();
    }else{
        $(elem_htm).hide();
    }
}


/********************************************************************/
//
/********************************************************************/
function openAddressModal(ids){
    $("#editAddressModal-"+ids).modal('show');
}

function openAccountsModal(ids){
    $("#editAccountsModal-"+ids).modal('show');
}

/********************************************************************/
//
/********************************************************************/
function delete_address(ids){
    ids = $("#table-"+ids).find("label.address_label_1").find("input").attr("id");
    id = ids.replace("id_form_","").replace("-is_shipping_address","");
    
    $.get("/contacts/delete_address/"+id+"/", function(data){
        if(data == '1') location.reload();
        else alert("Unauthorized Access");
    });
} 

/********************************************************************/
// 
/********************************************************************/
function delete_accounts(ids){
    ids = $("#table-"+ids).find(".account_holder_name").find("input").attr("id");
    id = ids.replace("id_form_","").replace("-account_holder_name","");
    
    
    $.get("/contacts/delete_accounts/"+id+"/", function(data){
        if(data == '1') location.reload();
        else alert("Unauthorized Access");
    });
}


function check() {
    if (getLocalStorageValue('form_errors_email') &&
    getLocalStorageValue('form_errors_phone') &&
    getLocalStorageValue('form_errors_pan') &&
    getLocalStorageValue('form_errors_gst') &&
    getLocalStorageValue('form_errors_url') &&
    getLocalStorageValue('form_errors_ifsc')){
        $(".save_button").prop("disabled",false);
        return true;
    }else{
        $(".save_button").prop("disabled",true);
        return false;
    } 
    
}

/************************************************************ */
// code by Lawrence - Ended
/************************************************************ */


/* Below Code By Roshan*/

/********************************************************************/
// GST NUMBER SHOW AND HIDE
/********************************************************************/
function hide_gst(elem){
    var a = $('#gst_reg :selected').text();
    if(a != "Not Applicable" & a != "---------" & a != "GST unregistered"){
        $("#gst_row").show()
        
    }
    else{
        $("#gst_row").hide()
    }
}



/********************************************************************/
// active, inactive and delete
/********************************************************************/

function status(a,c) {
    var status = 's'+a.toString()
    var b = document.getElementById(status).innerHTML;
    if(b.length == 13){
        $.ajax({
        type: 'GET',
        url: "/contacts/status_change/deactivate/"+a+"",
        success: function() {
            document.getElementById(a).innerHTML = 'clear'
            document.getElementById(status).innerHTML = 'Make Active'
            $('#'+'status'+a.toString()).modal('hide')
            document.getElementById('text').innerHTML = 'Are you sure you want to make '+c+' active '
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("some error");
        }

    });
    }
    if(b.length == 11){
        $.ajax({
        type: 'GET',
        url: "/contacts/status_change/activate/"+a+"",
        success: function() {
            document.getElementById(a).innerHTML = 'check'
            document.getElementById(status).innerHTML = 'Make Inactive'
            $('#'+'status'+a.toString()).modal('hide')
            document.getElementById('text').innerHTML = 'Are you sure you want to make '+c+' inactive '
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
var remove = 't'+c.toString()
$.ajax({
        type: 'GET',
        url: "/contacts/delete/"+c+"",
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