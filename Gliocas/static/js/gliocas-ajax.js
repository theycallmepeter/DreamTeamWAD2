
// $('#likeq').click(function(){
$(document).on('click','#likeq', function(){
	var questionslug;
	var like;
	questionslug = $(this).attr("data-questionslug");
	like = $(this).attr("data-like")
	$.get('/gliocas_app/likequestion/', {question_slug: questionslug, like: like}, function(data){
		switch (data){
			case "Unliked":
				$('#likeq.likeq').addClass("btn-outline-primary");	
				$('#likeq.likeq').removeClass("btn-primary");
				break;
			case "Undisliked":
				$('#likeq.dislikeq').addClass("btn-outline-danger");
				$('#likeq.dislikeq').removeClass("btn-danger");
				break;
			case "Liked":
				$('#likeq.likeq').addClass("btn-primary");
				$('#likeq.dislikeq').addClass("btn-outline-danger");
				$('#likeq.dislikeq').removeClass("btn-danger");
				break;
			case "Disliked":
				$('#likeq.dislikeq').addClass("btn-danger");
				$('#likeq.likeq').addClass("btn-outline-primary");
				$('#likeq.dislikeq').removeClass("btn-outline-danger");
				$('#likeq.likeq').removeClass("btn-primary");
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
				$('#likea.likea'+answerkey).addClass("btn-outline-primary");	
				$('#likea.likea'+answerkey).removeClass("btn-primary");
				break;
			case "Undisliked":
				$('#likea.dislikea'+answerkey).addClass("btn-outline-danger");
				$('#likea.dislikea'+answerkey).removeClass("btn-danger");
				break;
			case "Liked":
				$('#likea.likea'+answerkey).addClass("btn-primary");
				$('#likea.dislikea'+answerkey).addClass("btn-outline-danger");
				$('#likea.dislikea'+answerkey).removeClass("btn-danger");

				break;
			case "Disliked":
				$('#likea.dislikea'+answerkey).addClass("btn-danger");
				$('#likea.likea'+answerkey).addClass("btn-outline-primary");

				$('#likea.dislikea'+answerkey).removeClass("btn-outline-danger");
				$('#likea.likea'+answerkey).removeClass("btn-primary");
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
				$('#liker.liker'+replykey).addClass("btn-outline-primary");	
				$('#liker.liker'+replykey).removeClass("btn-primary");
				break;
			case "Undisliked":
				$('#liker.disliker'+replykey).addClass("btn-outline-danger");
				$('#liker.disliker'+replykey).removeClass("btn-danger");
				break;
			case "Liked":
				$('#liker.liker'+replykey).addClass("btn-primary");
				$('#liker.disliker'+replykey).addClass("btn-outline-danger");
				$('#liker.disliker'+replykey).removeClass("btn-danger");
				break;
			case "Disliked":
				$('#liker.disliker'+replykey).addClass("btn-danger");
				$('#liker.liker'+replykey).addClass("btn-outline-primary");

				$('#liker.disliker'+replykey).removeClass("btn-outline-danger");
				$('#liker.liker'+replykey).removeClass("btn-primary");
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
			$('#follow.follow' + courseslug).text('UNFOLLOW');
		} else {
			$('#follow.follow' + courseslug).text('FOLLOW');
			//thing to do if unfollowed
		}
	});
});

$(document).ready(function(){
	$('#form-div').hide()
	$('#cancel').hide()
	$('#cancelanswer').hide()
	$('.reply-body').each(function(){
		var replykey = $(this).attr("data-replykey")
		var upvotedclass = $(".voted"+replykey)
		var upvoted = upvotedclass.text()
		if(upvoted === "upvoted"){
			$('#liker.liker'+replykey).addClass("btn-primary");
			$('#liker.liker'+replykey).removeClass("btn-outline-primary");
		} else if (upvoted === "downvoted"){
			$('#liker.disliker'+replykey).addClass("btn-danger");
			$('#liker.disliker'+replykey).removeClass("btn-outline-danger");
		}
	})
	$('.answer-body').each(function(){
		var answerkey = $(this).attr("data-answerkey")
		var upvotedclass = $(".voteda"+answerkey)
		var upvoted = upvotedclass.text()
		console.log(answerkey)
		console.log(upvoted)
		if(upvoted === "upvoted"){
			$('#likea.likea'+answerkey).addClass("btn-primary");
			$('#likea.likea'+answerkey).removeClass("btn-outline-primary");
		} else if (upvoted === "downvoted"){
			$('#likea.dislikea'+answerkey).addClass("btn-danger");
			$('#likea.dislikea'+answerkey).removeClass("btn-outline-danger");

		}
	})
	$('.card-body').each(function(){
		var upvotedclass = $(".votedq")
		var upvoted = upvotedclass.text()
		if(upvoted === "True"){
			$('#likeq.likeq').addClass("btn-primary");
			$('#likeq.likeq').removeClass("btn-outline-primary");
		} else if (upvoted === "False"){
			$('#likeq.dislikeq').addClass("btn-danger");
			$('#likeq.dislikeq').removeClass("btn-outline-danger");

			$('#likeq.dislikeq').addClass("btn-danger");
		}
	})
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
	$('#cancelreply').hide()
	$('.reply'+answerkey).show()
});

$(document).on('click','#reply', function(){
	var answerkey
	answerkey = $(this).attr("data-answerkey");
	$('.reply_form'+answerkey).show()
	$('.cancel'+answerkey).show()
});

$(document).on('click','#answer', function(){
	$('#cancelanswer').show()
	$('#answer_form').show()
	$('#answer').hide()
});

$(document).on('click','#cancelanswer', function(){
	$('#answer_form').hide()
	$('#answer').show()
	$('#cancelanswer').hide()
});