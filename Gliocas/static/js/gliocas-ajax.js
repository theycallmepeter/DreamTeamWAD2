
// $('#likeq').click(function(){
$(document).on('click','#likeq', function(){
	var questionslug;
	var like;
	questionslug = $(this).attr("data-questionslug");
	like = $(this).attr("data-like")
	$.get('/gliocas_app/likequestion/', {question_slug: questionslug, like: like}, function(data){
		switch (data){
			case "Unliked":
				$('#likeq.likeq').removeClass("btn-success");
				break;
			case "Undisliked":
				$('#likeq.dislikeq').removeClass("btn-danger");
				break;
			case "Liked":
				$('#likeq.likeq').addClass("btn-success");
				$('#likeq.dislikeq').removeClass("btn-danger");
				break;
			case "Disliked":
				$('#likeq.dislikeq').addClass("btn-danger");
				$('#likeq.likeq').removeClass("btn-success");
				break;
		};
	});
});

$(document).on('click','#likea', function(){
	var answerkey;
	var like;
	answerkey = $(this).attr("data-answerkey");
	like = $(this).attr("data-like")
	$.get('/gliocas_app/likeanswer/', {answer_key: answerkey, like: like}, function(data){
		switch (data){
			case "Unliked":
				$('#likea.likea'+answerkey).removeClass("btn-success");
				break;
			case "Undisliked":
				$('#likea.dislikea'+answerkey).removeClass("btn-danger");
				break;
			case "Liked":
				$('#likea.likea'+answerkey).addClass("btn-success");
				$('#likea.dislikea'+answerkey).removeClass("btn-danger");
				break;
			case "Disliked":
				$('#likea.dislikea'+answerkey).addClass("btn-danger");
				$('#likea.likea'+answerkey).removeClass("btn-success");
				break;
		};
	});
});

$(document).on('click','#liker', function(){
	var replykey;
	var like;
	replykey = $(this).attr("data-replykey");
	like = $(this).attr("data-like")
	jQuery.get('/gliocas_app/likereply/', {reply_key: replykey, like: like}, function(data){
		switch (data){
			case "Unliked":
				$('#liker.liker'+replykey).removeClass("btn-success");
				break;
			case "Undisliked":
				$('#liker.disliker'+replykey).removeClass("btn-danger");
				break;
			case "Liked":
				$('#liker.liker'+replykey).addClass("btn-success");
				$('#liker.disliker'+replykey).removeClass("btn-danger");
				break;
			case "Disliked":
				$('#liker.disliker'+replykey).addClass("btn-danger");
				$('#liker.liker'+replykey).removeClass("btn-success");
				break;
		};
	});
});

$(document).on('click','#follow', function(){
	var courseslug;
	courseslug = $(this).attr("data-courseslug");
	subjectslug = $(this).attr("data-subjectslug");
	jQuery.get('/gliocas_app/followcourse/', {course_slug: courseslug, subject_slug:subjectslug}, function(data){
		if (data==="Followed"){
			//thing to do if followed
			$('#follow').text('UNFOLLOW');
		} else {
			$('#follow').text('FOLLOW');
			//thing to do if unfollowed
		}
	});
});

$(document).ready(function(){
	$('#form-div').hide()
	$('#answer_form').hide()
	$('#cancel').hide()
});

$(document).on('click','#ask-question', function(){
	$('#form-div').show()
	$('#ask-question').hide()
});

$(document).on('click','#cancel', function(){
	$('#form-div').hide()
	$('#ask-question').show()
});

$(document).on('click','#cancelreply', function(){
	var answerkey
	answerkey = $(this).attr("data-answerkey");
	$('.reply_form'+answerkey).hide()
	$('.reply'+answerkey).show()
});

$(document).on('click','#reply', function(){
	var answerkey
	answerkey = $(this).attr("data-answerkey");
	$('.reply_form'+answerkey).show()
	$('.cancel'+answerkey).show()
});

$(document).on('click','#answer', function(){
	$('#answer_form').show()
});
