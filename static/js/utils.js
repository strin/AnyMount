// basic functions.
function write_cloud_logo(path, name) {
  if(name == "dropbox") {
    document.write("<img src='"+path+"img/dropbox.png' width='32px'></img>");
  }
}

function toggle_element(id) {
  if($(id).css('display') == 'none') {
    toggle_on(id);
  }else{
    toggle_off(id);
  }
}

function toggle_on(id) {
  if($(id).css('display') == 'none') {
    $(id).slideDown('slow');
    // $(id).css('display', 'block');
  }
}

function toggle_off(id) {
  if($(id).css('display') == 'block') {
    $(id).slideUp('slow');
    // $(id).css('display', 'none');
  }
}