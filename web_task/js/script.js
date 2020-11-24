// 绑定按钮事件
window.onload = function()
{
    let button_click = document.getElementById("btn1");
    button_click.onclick = process_input
};

function offline(material_id){
    if(!confirm(material_id + "将被下线")){
        return
    }
    const url = 'http://test.sogou.com/img_offline?mid=' + material_id;
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (request.readyState===4){
            // if(request.status===200){
            if(1){
                document.getElementById("button_" + material_id).setAttribute("disabled", "disabled");
            }else{
                alert("下线失败，服务端无响应！")
            }
        }
    };
    request.open("GET", url, true);
    request.send();
}

// 处理输入，展现内容
function process_input()
{
    let textarea = document.getElementById("textarea1");
    if(textarea.value.trim().length === 0){
        textarea.value = '';
        return
    }

    let content = '<table><tbody><tr class=table id=table1><td>物料ID</td><td>触发词</td><td>图片</td><td>操作</td></tr>';
    const lines = textarea.value.split("\n");
    for(let line of lines){
        let elements = line.split("\t");
        if(elements.length !== 3) {
            if(elements.length !== 0){
                console.warn(line);
                continue;
            }
        }
        content += "<tr id='" + elements[0] + "'>";
        content += '<td>'+elements[0]+'</td>' + '<td>'+elements[1]+'</td>';
        content += "<td><img alt='image' src='" + elements[2] + "'></td>";
        content += "<td><button type='button' id='button_" + elements[0] + "' onclick='offline(" + elements[0]+ ")'/>下线</td>";
    }
    let result_table = document.getElementById("result");
    result_table.innerHTML = content;
}


