
/*
 * GET home page.
 */

var markdown = require('markdown').markdown

exports.index = function(req, res){
  res.render('index', { title: 'Express' });
};
exports.numAnalysis = function(req, res){
  res.render('numAnalysis', { title: 'Numerical Analysis' });
};

exports.numAnalysisPage = function(req, res){
    res.render('numAnalysis/'+req.params.id+'.md', {title: req.params.id})
};


exports.modern = function(req, res){
  res.render('modern', { title: 'Modern Physics' });
};
exports.class = function(req, res){
  res.render('index', { title: 'Express' });
};
