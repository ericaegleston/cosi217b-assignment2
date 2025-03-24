function showCommentForm() {
    var form = document.getElementById("add_comment_container");
    if (form.style.display === "block") {
      form.style.display = "none";
    } else {
      form.style.display = "block";
    }
  }