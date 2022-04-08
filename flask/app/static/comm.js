var glob_id = null;

window.onload = function() {
  glob_id = null;
};

function send_response(id_str, sentiment) {
    if (glob_id == null) {
        glob_id = id_str
    }
    let id = parseInt(glob_id)
    if (typeof (id) === 'number' && id > 0 && id < 200000) {
        let req = new XMLHttpRequest();
        req.open('POST', 'http://54.174.185.69:80/update_news', true);
        req.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        req.send(JSON.stringify({"id": id, "sentiment": sentiment}));
        req.onreadystatechange = function (aEvt) {
            if (req.readyState == 4) {
                if (req.status == 200) {
                    console.log((req.response));
                    update_content();
                } else {
                    console.error("Error loading page\n");
                }
            }
        };
    } else {
        console.warn("what are you trying!")
    }
}

function update_content(){
    let req = new XMLHttpRequest();
        req.open('GET', 'http://54.174.185.69:80/update_news', true);
        req.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        req.send();
        req.onreadystatechange = function (aEvt) {
            if (req.readyState == 4) {
                if (req.status == 200) {
                    let jsonResponse = JSON.parse(req.responseText);
                    console.log(jsonResponse)
                    document.getElementById("news_content").innerHTML = jsonResponse.content;
                    glob_id = jsonResponse['id'];
                } else {
                    console.error("Error loading page\n");
                }
            }
        };
}
