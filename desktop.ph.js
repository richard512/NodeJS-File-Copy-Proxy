var system = require('system');
var args = system.args;
var webPage = require('webpage');
var page = webPage.create();

if (args.length != 2) {
	phantom.exit()
}

page.settings.userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.71 Safari/537.36';

page.viewportSize = { width: 1366, height: 768 };
page.open(args[1], function start(status) {
	page.evaluate(function() {
		if (!document.body.bgColor) document.body.bgColor = 'white';
	});

	setTimeout(function(){
		page.render('desktop.png');
		phantom.exit();
	}, 1000);
});
