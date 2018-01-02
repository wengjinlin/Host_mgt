$(function () {
    $('#add_group').click(function () {
       var show_div = $('#_group');
       $('.mask', window.parent.document).removeClass("hidden");
       $('.mask').removeClass("hidden");
       show_div.removeClass("hidden");
       show_div.find('a').eq(1).addClass("hidden");
    });
    $('[name="del_group"]').click(function () {
       var groupname = $(this).parent().parent().siblings().eq(1).text();
       var con=confirm("确定删除"+groupname+"吗？");
       if(!con){
           return false;
       }
    });
    $('[name="modify_group"]').click(function () {
        var groupname = $(this).parent().parent().siblings().eq(1).text();
        var group_id = $(this).attr("group_id");
        var show_div = $('#_group');
        $('.mask', window.parent.document).removeClass("hidden");
        $('.mask').removeClass("hidden");
        show_div.removeClass("hidden");
        show_div.find('a').eq(0).addClass("hidden");
        show_div.find('[name="groupname"]').val(groupname);
        show_div.find('[name="group_id"]').val(group_id);
    });
});
function submitForm_g(){
    $('#form_group').form('submit',{
        onSubmit:function(){
            return $(this).form('enableValidation').form('validate');
        },
        success:function(){
            clearForm_g();
            $('#group_mgt', window.parent.document).attr('src', $('#group_mgt', window.parent.document).attr('src'));
        }
    });
}
function clearForm_g(){
    $('#form_group').form('clear');
    $('.mask').addClass("hidden");
    $('.mask', window.parent.document).addClass("hidden");
    $('#_group').find('a').each(function () {
        $(this).removeClass("hidden")
    });
    $('#_group').addClass("hidden");
}