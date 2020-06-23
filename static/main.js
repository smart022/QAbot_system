function gen_sent(user,name,str){
    var $head_icon = $("<img class='headIcon radius'/>")
    if(user)
        var $sent = $("<div class='cright cmsg'></div>")
    else
        var $sent = $("<div class='cleft cmsg'></div>")

    //<img src="http://ww1.sinaimg.cn/thumbnail/d3e3f003gy1gg2l3njzrzj207g07g74c.jpg"/>
    // http://ww1.sinaimg.cn/mw690/d3e3f003gy1gg2l9vogamj2069069t8n.jpg
    $head_icon.attr('src',"http://ww1.sinaimg.cn/mw690/d3e3f003gy1gg2l9vogamj2069069t8n.jpg")

    $sent.append($head_icon)
    var $name = $("<span class='name'></span>").text(name)
    $sent.append($name)
    return $sent.append($("<span class='content'></span>").text(str))
}
function addLine(gen_ele){
    $('.lite-chatbox').append(gen_ele);
}
function gen_info(lvl,info){
    //tips	正常
    let tips = new Map([
    [0,"tips-primary"],//	首要的提示
    [1,"tips-success"],//	成功提示
    [2,"tips-info"],	//信息提示
    [3,"tips-warning"],//	警告提示
    [4,"tips-danger"]	//错误/危险提示
    ]);
    var $info = $("<div class='tips'></div>");
    
    var $detail = $('<span></span>').text("系统消息："+info)
    console.log(tips[lvl])
    $detail.addClass(tips.get(lvl))

    $info.append( $detail )
    return $info
}

function scrollToEnd(){//滚动到底部
    var h = $(document).height()-$(window).height();
    $(document).scrollTop(h); 
}

$(function () {
    let socketio = io();  // 创建 socket 实例

    socketio.on("connect",function(){
        console.log('connected!')
        addLine(gen_info(1,"connect successful!!"))
    })

    socketio.on("system-message",function(data){
        //console.log('user got ',data)
        addLine(gen_info(1,"connect successful!!"))
        scrollToEnd()
    })

    socketio.on("chat-message",function(data){
        console.log('user got ',data)
        addLine(gen_sent(false,'bot',data))
        scrollToEnd()
    })


    
    $('#form').submit(function(e){
        //alert("Submitted");
        e.preventDefault();
        socketio.emit('chat-message', $('#input_txt').val());
        //console.log('user:',$('#input_txt').val())
        
        let gen_ele= gen_sent(true,'user', $('#input_txt').val())
        addLine(gen_ele)
        $('#input_txt').val("");
        return false;
    });

   
});