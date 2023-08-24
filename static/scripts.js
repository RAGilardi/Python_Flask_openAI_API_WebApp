$('#message').keydown(function(event) {
    if (event.keyCode == 13 && event.shiftKey) {
      var content = this.value;
      var caret = getCaret(this);
      this.value = content.substring(0,caret)+"\n"+content.substring(caret,content.length-1);
      event.stopPropagation();
    } else if (event.keyCode == 13) {
      $('#chat-input').submit();
      event.preventDefault();
    }
  });

  function getCaret(el) {
    if (el.selectionStart) {
      return el.selectionStart;
    } else if (document.selection) {
      el.focus();
      var r = document.selection.createRange();
      if (r == null) {
        return 0;
      }
      var re = el.createTextRange(), rc = re.duplicate();
      re.moveToBookmark(r.getBookmark());
      rc.setEndPoint('EndToStart', re);
      return rc.text.length;
    }
    return 0;
  }

  $('form').submit(function(event) {
    event.preventDefault();
    $.post('/chatbot', $(this).serialize(), function(response) {
      $('#chat').append(response);
      $('#message').val('').focus();
    });
  });