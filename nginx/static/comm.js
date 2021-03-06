let glob_id = null;

window.onload = function() {
  glob_id = null;
};

let glow = $('.ss-main');
setInterval(function(){
    glow.hasClass('glow') ? glow.removeClass('glow') : glow.addClass('glow');
}, 5000);

function send_response(id_str, sentiment) {
    if (glob_id == null) {
        glob_id = id_str
    }
    let id = parseInt(glob_id)
    if (typeof (id) === 'number' && id > 0 && id < 200000 && (sentiment == 0 | sentiment == 1 | sentiment == 2)) {
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
        console.warn("Invalid input data for ID: ".concat(id_str).concat(" SENTIMENT: ").concat(sentiment))
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
