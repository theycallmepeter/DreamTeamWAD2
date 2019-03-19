
$('#likeq').click(function(){
	var questionslug;
	questionslug = $(this).attr("data-questionslug");
	like = $(this).attr("like")
	if (like){
		$.get('/gliocas_app/likequestion/1/', {question_slug: questionslug}, function(data){
			$('#like_count').html(data);
				//change to change colour of like button
				// $('#like').hide();
		});
	} else {
		$.get('/gliocas_app/likequestion/0/', {question_slug: questionslug}, function(data){
			$('#like_count').html(data);
				//change to change colour of like button
				// $('#like').hide();
		});
	}
});

$('#likea').click(function(){
	var answerkey;
	answerkey = $(this).attr("data-answerkey");
	like = $(this).attr("like")
	$.get('/gliocas_app/likeanswer/', {answer_key: answerkey}, function(data){
		$('#like_count').html(data);
			//change to change colour of like button
			// $('#like').hide();
	});
});

$('#liker').click(function(){
	var replykey;
	var like;
	replykey = $(this).attr("data-replykey");
	like = $(this).attr("like")
	$.get('/gliocas_app/likereply/', {reply_slug: replykey}, function(data){
		$('#like_count').html(data);
			//change to change colour of like button
			// $('#like').hide();
	});
});
