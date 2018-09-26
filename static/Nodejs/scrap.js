const puppeteer = require('puppeteer');
const $ = require('cheerio');
const url = 'file:///home/quiles/Documents/sculpt/www.skulpt.org/index.html#';
var fs = require('fs');

puppeteer
  .launch()
  .then(function(browser) {
    return browser.newPage();
  })
  .then(function(page) {
    return page.goto(url).then(function() {
      return page.content();
    });
  })
  .then(function(html) {
    $('#code', html).each(function() {
     fs.writeFile('tryt',$(this).text(), function(err) {
    if(err) {
        return console.log(err);
    }

    console.log("The file was saved!");
}); 
    });
  })
  .catch(function(err) {
    //handle error
});


