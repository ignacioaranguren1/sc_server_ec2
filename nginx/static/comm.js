let glob_id = null;

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
        req.open('POST', 'https://'.concat(location.hostname).concat(":").concat(location.port).concat('/update_news'), true);
        req.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        req.send(JSON.stringify({"id": id, "sentiment": sentiment}));
        req.onreadystatechange = function (aEvt) {
            if (req.readyState == 4) {
                if (req.status == 200) {
                    console.log((req.response));
                    update_content();
                } else if (req.status == 232){
                    console.warn(req.response)
                }
                else {
                    console.error("Error loading page\n");
                }
            }
        };
    } else {
        console.warn("Invalid id")
    }
}

function update_content(){
    let req = new XMLHttpRequest();
        req.open('GET', 'https://'.concat(location.hostname).concat(":").concat(location.port).concat('/update_news'), true);
        req.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        req.send();
        open_modal()
        req.onreadystatechange = function (aEvt) {
            if (req.readyState == 4) {
                if (req.status == 200) {
                    let jsonResponse = JSON.parse(req.responseText);
                    console.log(jsonResponse)
                    document.getElementById("news_content").innerHTML = jsonResponse.content;
                    glob_id = jsonResponse['id'];
                    close_modal()
                } else {
                    console.error("Error loading page\n");
                    close_modal()
                }
            }
        };
}

let modal = document.getElementById("modal");

// When the user clicks the button, open the modal
function open_modal() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
function close_modal() {
  modal.style.display = "none";
}
