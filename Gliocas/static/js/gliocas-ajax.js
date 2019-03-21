
// $('#likeq').click(function(){
$(document).on('click','#likeq', function(){
	var questionslug;
	var like;
	questionslug = $(this).attr("data-questionslug");
	like = $(this).attr("data-like")
	$.get('/gliocas_app/likequestion/', {question_slug: questionslug, like: like}, function(data){
		// $('#like_count').html(data);
		//put code to change style of likebutton here
	});
});

$(document).on('click','#likea', function(){
	var answerkey;
	var like;
	answerkey = $(this).attr("data-answerkey");
	like = $(this).attr("data-like")
	$.get('/gliocas_app/likeanswer/', {answer_key: answerkey, like: like}, function(data){
		// $('#like_count').html(data);
		//put code to change style of likebutton here
	});
});

$(document).on('click','#liker', function(){
	var replykey;
	var like;
	replykey = $(this).attr("data-replykey");
	like = $(this).attr("data-like")
	$.get('/gliocas_app/likereply/', {reply_key: replykey, like: like}, function(data){
		// $('#like_count').html(data);
		//put code to change style of likebutton here
	});
});

$(document).on('click','#follow', function(){
	var courseslug;
	courseslug = $(this).attr("data-courseslug");
	subjectslug = $(this).attr("data-subjectslug");
	$.get('/gliocas_app/followcourse/', {course_slug: courseslug, subject_slug:subjectslug}, function(data){
		if (data==="Followed"){
			//thing to do if followed
			$('#follow').text('Unfollow this course');
		} else {
			$('#follow').text('Follow this course');
			//thing to do if unfollowed
		}
	});
});

$(document).ready(function(){
	$('#form-div').hide()
});

$(document).on('click','#ask-question', function(){
	$('#form-div').show()
	$('#ask-question').hide()
});

$(document).on('click','#cancel', function(){
	$('#form-div').hide()
	$('#ask-question').show()
});

// var form = $('#question_form');
//     form.submit(function (event) {
//     	event.preventDefault();
// 	    console.log("form submitted!");  // sanity check
// 	    return false;
//     //     $.ajax({
//     //         type: "POST",
//     //         url: form.attr('action'),
//     //         data: form.serialize(),
//     //         success: function (data) {
//     //             $('#form-div').hide()
// 				// $('#ask-question').show()
//     //         },
//     //         error: function(data) {
//     //         	$('#form-div').hide()
// 				// $('#ask-question').show()
//     //             console.log("Didn't submit correctly.")
//     //         }
//     //     });
//     //     return false;
//     });