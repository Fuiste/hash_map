!function ($, _H, Em) {
  $(function(){

    window.App = Em.Application.create({
      LOG_TRANSITIONS: true,
      ENABLE_ALL_FEATURES: true,
      LOG_ACTIVE_GENERATION: true,
      LOG_VIEW_LOOKUPS: true
    });

    App.ApplicationAdapter = DS.DjangoRESTAdapter.extend({
      namespace: 'api'
    });
    App.ApplicationSerializer = DS.DjangoRESTSerializer.extend({
      namespace: 'api'
    });

    App.SessionController = Ember.ObjectController.extend({
      email: null,
      password: null,
      errorMessage: null,
      reset: function() {
        this.setProperties({
          email: null,
          password: null,
          errorMessage: null,
          model: null
        });
      },
      isAuthenticated: function() {
        return !Em.isEmpty(this.get('model'));
      }.property('model'),
      setCurrentUser: function(userId) {
        if (!Em.isEmpty(userId)) {
          var currentUser = this.store.find('user', userId);
          this.set('model', currentUser);
        }
      },
      actions: {
        login: function() {
          var self = this, data = this.getProperties('email', 'password');
          $.post('/session/', data).then(function(response) {
            self.setCurrentUser(response.userId);
            if (!('message' in response)) {
              self.transitionToRoute('home');
            }
            self.set('errorMessage', response.message);
          });
        },
        logout: function() {
          $.ajax({
            url: '/session/',
            type: 'delete',
            beforeSend: function(xhr) {
              xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
            }
          });
          this.reset();
          this.transitionTo('index');
        }
      }
    });
    App.AuthorizedAccessController = Em.Controller.extend({
      unauthorized: false,
      incorrect: false
    });
    App.LoginRoute = Em.Route.extend({
      beforeModel: function(){
        this._super();
        if (this.controllerFor('session').get('isAuthenticated')){
          this.transitionTo('albums');
        }
      },
      afterModel: function(){
        $(document).attr('title', 'App - Login');
      }
    });
    App.LoginController = Em.Controller.extend({
      needs: ['application', 'authorizedAccess'],
      actions: {}
    });

    App.Router.map(function() {
      this.resource('session');
      this.resource('index', {path: '/'});
      this.resource('login', {path: '/login'});
      this.resource('home');
    });
    // Application Route and Controller
    App.ApplicationRoute = Em.Route.extend({
      beforeModel: function() {
        var self = this;
        return Ember.RSVP.Promise.resolve(Em.$.getJSON('/session/')).then(function(response) {
          self.controllerFor('session').setCurrentUser(response.userId);
        });
      }
    });
    App.ApplicationController = Em.Controller.extend({
      needs: ['session']
    });
    // All subsequent controllers can extend this guy and access the session controller
    App.SController = Em.Controller.extend({
      needs: ['session']
    });

    App.AuthenticatedRoute = Em.Route.extend({
      needs: ['authorizedAccess'],
      beforeModel: function(transition) {
        if (!(this.controllerFor('session').get('isAuthenticated'))) {
          this.controllerFor('authorizedAccess').set('unauthorized', true);
          return this.transitionTo('login');
        }
        var csrftoken = getCookie('csrftoken');
        $.ajaxSetup({
          traditional: true,
          crossDomain: false, // obviates need for sameOrigin test
          beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
              xhr.setRequestHeader('X-CSRFToken', csrftoken);
            }
          }
        });
        return true;
      }
    });

    App.HomeRoute = App.AuthenticatedRoute.extend({});

  });
}(window.jQuery, window.Handlebars, window.Ember);
