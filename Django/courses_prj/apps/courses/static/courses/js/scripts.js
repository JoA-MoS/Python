$('#delete').click(function () {

    var id = $('#delete').attr('data-course-id');
    var url = `/courses/${id}/delete/`;
    console.log(url);
    return sendDelete(url);
})


function sendDelete(delUrl) {
    $.ajax({
        type: "DELETE",
        url: delUrl,
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", $.cookie("csrftoken"));
        },
        success: function (msg) {
            return true
        },
        error: function (msg) {
            return false
        }
    });
}
