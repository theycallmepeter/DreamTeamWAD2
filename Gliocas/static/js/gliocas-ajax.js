
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