$(function(){

  var A = App;
  var m = DS.Model;
  var a = DS.attr;

  A.User = m.extend({
    email: a('string')
  });

  A.Answer = m.extend({
    text: a('string'),
    grade: a('number')
  });

  A.Assignment = m.extend({
    shopper: DS.belongsTo('shopper'),
    survey: DS.belongsTo('survey'),
    responses: DS.hasMany('surveyResponse'),
    done: a('boolean')
  });

  A.Category = m.extend({
    name: a('string'),
    subcategories: DS.hasMany('subcategory')
  });

  A.Manager = m.extend({
    email: a('string'),
    propertyPreferences: DS.hasMany('propertyPreference')
  });

  A.Property = m.extend({
    name: a('string')
  });

  A.PropertyPreference = m.extend({
    property: DS.belongsTo('property'),
    notifyNewSurvey: a('boolean'),
    notifySurveyAccept: a('boolean')
  });

  A.Question = m.extend({
    text: a('string'),
    scale: DS.belongsTo('scale'),
    scored: a('boolean'),
    notApplicable: a('boolean')
  });

  A.SurveyResponse = m.extend({
    question: DS.belongsTo('question'),
    answer: DS.belongsTo('answer'),
    text: a('string'),
    notApplicable: a('string')
  });

  A.Scale = m.extend({
    answers: DS.hasMany('answer'),
    name: a('string')
  });

  A.Shopper = m.extend({
    email: a('string')
  });

  A.Subcategory = m.extend({
    name: a('string'),
    questions: DS.hasMany('question')
  });

  A.Survey = m.extend({
    surveyItems: DS.hasMany('surveyItem'),
    name: a('string'),
    flavorText: a('string'),
    showSections: a('boolean')
  });

  A.SurveyItem({
    question: DS.belongsTo('question'),
    position: a('number')

});
