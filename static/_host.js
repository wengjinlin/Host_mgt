$(function () {
    // $('#add_host').click(function () {
    //    var show_div = $('#_host', window.parent.document);
    //    $('.mask', window.parent.document).removeClass("hidden");
    //    show_div.removeClass("hidden");
    //    show_div.find('a').eq(1).addClass("hidden");
    // });
    $.extend($.fn.validatebox.defaults.rules, {
        ip: {
            validator: function(value,param){
                var reg = /^((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)/g;
                return reg.test(value);
            },
            message: '请输入正确的IP地址！'
        },
        onlyNum:{
            validator:function(value,param){
                var reg = /^\d+$/g;
                return reg.test(value);
            },
            message:  '只能输入数字！'
        }
    });
    $('#add_host').click(function () {
       var show_div = $('#_host');
       $('.mask', window.parent.document).removeClass("hidden");
       $('.mask').removeClass("hidden");
       show_div.removeClass("hidden");
       show_div.find('a').eq(1).addClass("hidden");
    });
    $('[name="del_host"]').click(function () {
       var hostname = $(this).parent().parent().siblings().eq(1).text();
       var con=confirm("确定删除"+hostname+"吗？");
       if(!con){
           return false;
       }
    });
    $('[name="modify_host"]').click(function () {
        var hostname = $(this).parent().parent().siblings().eq(1).text();
        var ip = $(this).parent().parent().siblings().eq(2).text();
        var port = $(this).parent().parent().siblings().eq(3).text();
        var os = $(this).parent().parent().siblings().eq(4).text();
        var group = $(this).parent().parent().siblings().eq(5).text();
        var host_id = $(this).attr("host_id");
        var show_div = $('#_host');
        $('.mask', window.parent.document).removeClass("hidden");
        $('.mask').removeClass("hidden");
        show_div.removeClass("hidden");
        show_div.find('a').eq(0).addClass("hidden");
        show_div.find('[name="hostname"]').val(hostname);
        show_div.find('[name="ip"]').val(ip);
        show_div.find('[name="port"]').val(port);
        show_div.find('[name="os"]').val(os);
        show_div.find('[name="hostgroup"]').val(group);
        show_div.find('[name="host_id"]').val(host_id);
    });
});
function submitForm(){
    $('#form_host').form('submit',{
        onSubmit:function(){
            return $(this).form('enableValidation').form('validate');
        },
        success:function(){
            clearForm();
            $('#host_mgt', window.parent.document).attr('src', $('#host_mgt', window.parent.document).attr('src'));
        }
    });
}
function clearForm(){
    $('#form_host').form('clear');
    $('.mask').addClass("hidden");
    $('.mask', window.parent.document).addClass("hidden");
    $('#_host').find('a').each(function () {
        $(this).removeClass("hidden")
    });
    $('#_host').addClass("hidden");
}