function process_input()
// 处理输入，展现内容
{
    let textarea = document.getElementById("textarea1");
    if(textarea.value.trim().length === 0){
        textarea.value = ''
        return
    }

    let content = ''
    const lines = textarea.value.split("\n")
    for(let line of lines){
        let elements = line.split("\t")
        if(elements.length !== 3) {
            console.log(line)
            continue
        }
        let temp_row = "<tr id='" + elements[0] + "'>"
        content
    }



}

// 绑定按钮事件
window.onload = function()
{
    let button_click = document.getElementById("btn1")
    button_click.onclick = process_input
}


