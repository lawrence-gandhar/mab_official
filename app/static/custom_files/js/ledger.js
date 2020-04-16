
function get_predefined_groups(elem){

    if($(elem).val()!=""){

        var ids = $(elem).val();
        ajax_get_predefined_groups(ids);

    }else{
        $("#id_acc_group").empty().append('<option value="">-----</option>');
    }
}

function ajax_get_predefined_groups(ids){
    $.get("/get_predefined_groups/",{"ids":ids}, function(data){
        $("#id_acc_group").empty().append(data);
    });
}

/**********************************************************/
//
/**********************************************************/

function openNewGroupModal(elem){
    if($(elem).val() == -1){
        $("#major_head_ins").val($("#id_major_heads").val())
        $("#addGroupModal").modal('show');
    }
}

function add_group_form(save_type){
    $.post("/add_ledger_group/",$("#add_group_form").serialize(), function(data){
        if(data != '0'){
            ajax_get_predefined_groups($("#id_major_heads").val());
            $("#addGroupModal").modal('hide');
        }
    });
}
