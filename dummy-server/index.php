<?php

include_once 'Request.php';
include_once 'Router.php';

$router = new Router(new Request);

// Start Conversation
$router->get('/api/conversation/start', function() {
	return json_encode([
		"cid" => 0
	]);
});

// End Conversation
$router->post('/api/conversation/end/0', function($request) {
	return;
});

// Flag Conversation
$router->get('/api/conversation/flag/0', function() {
	return;
});

// Send Message
$router->post('/api/conversation/send/0', function($request) {
	return;
});

// Receive Message
$router->get('/api/conversation/receive/0', function() {
	return json_encode([
		"cid" => 0,
		"messages" => [
			[
				"id" => 0,
				"text" => "Hello World!",
				"timestamp" => "2020-01-01 00:00:00"
			]
		]
	]);
});

// Get Leaderboards
$router->get('/api/leaderboards', function() {
	return json_encode([
		"users" => [
			[
				"rank" => 0,
				"username" => "user1",
				"score" => 0.95
			],
			[
				"rank" => 1,
				"username" => "user2",
				"score" => 0.80
			],
			[
				"rank" => 2,
				"username" => "user3",
				"score" => 0.79
			],
			[
				"rank" => 3,
				"username" => "user4",
				"score" => 0.52
			],
			[
				"rank" => 4,
				"username" => "user5",
				"score" => 0.00
			]
		]
	]);
});

?>
