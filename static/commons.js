$(function () {
   // $.extend($.fn.validatebox.defaults.rules, {
   //      ip: {
   //          validator: function(value,param){
   //              var reg = /^((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)/g;
   //              return reg.test(value);
   //          },
   //          message: '请输入正确的IP地址！'
   //      },
   //      onlyNum:{
   //          validator:function(value,param){
   //              var reg = /^\d+$/g;
   //              return reg.test(value);
   //          },
   //          message:  '只能输入数字！'
   //      }
   //  });
   $('#tt').tabs({
        border:false,
        onSelect:function(title,index){
            if(title == "主机管理"){
                $('#host_mgt').attr('src', $('#host_mgt').attr('src'));
            }
            if(title == "分组管理"){
                $('#group_mgt').attr('src', $('#group_mgt').attr('src'));
            }
        }
    });
});
// function submitForm(){
//     $('#form_host').form('submit',{
//         onSubmit:function(){
//             return $(this).form('enableValidation').form('validate');
//         },
//         success:function(){
//             clearForm();
//             $('#host_mgt').attr('src', $('#host_mgt').attr('src'));
//         }
//     });
// }
// function submitForm_g(){
//     $('#form_group').form('submit',{
//         onSubmit:function(){
//             return $(this).form('enableValidation').form('validate');
//         },
//         success:function(){
//             clearForm_g();
//             $('#group_mgt').attr('src', $('#group_mgt').attr('src'));
//         }
//     });
// }
// function clearForm(){
//     $('#form_host').form('clear');
//     $('.mask').addClass("hidden");
//     $('#_host').find('a').each(function () {
//         $(this).removeClass("hidden")
//     });
//     $('#_host').addClass("hidden");
// }
// function clearForm_g(){
//     $('#form_group').form('clear');
//     $('.mask').addClass("hidden");
//     $('#_group').find('a').each(function () {
//         $(this).removeClass("hidden")
//     });
//     $('#_group').addClass("hidden");
// }
function addTab(title, url){
    if ($('#tt').tabs('exists', title)){
        $('#tt').tabs('select', title);
        if(title == "主机管理"){
            $('#host_mgt').attr('src', $('#host_mgt').attr('src'));
        }
        if(title == "分组管理"){
            $('#group_mgt').attr('src', $('#group_mgt').attr('src'));
        }
    } else {
        var content = "";
        if(title == "主机管理"){
            content = '<iframe id="host_mgt" scrolling="auto" frameborder="0"  src="'+url+'" style="width:100%;height:100%;position: absolute;z-index: 52;"></iframe>';
        }
        if(title == "分组管理"){
            content = '<iframe id="group_mgt" scrolling="auto" frameborder="0"  src="'+url+'" style="width:100%;height:100%;position: absolute;z-index: 52;"></iframe>';
        }
        $('#tt').tabs('add',{
            title:title,
            content:content,
            closable:true
        });
    }
}