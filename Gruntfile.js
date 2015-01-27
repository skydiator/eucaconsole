
module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
      pkg: grunt.file.readJSON('package.json'),
      bowercopy: {
          options: {
              // Bower components folder will be removed afterwards
              clean: true
          },
          angular: {
              options: {
                  destPrefix: 'eucaconsole/static/js/thirdparty/angular'
              },
              files: {
                'angular.min.js': 'angular/angular.min.js',
                'angular-sanitize.min.js': 'angular-sanitize/angular-sanitize.min.js',
                'angular-mocks.js': 'angular-mocks/angular-mocks.js'
              }
          },
          jquery: {
              options: {
                  destPrefix: 'eucaconsole/static/js/thirdparty/jquery'
              },
              files: {
                'jquery.min.js': 'jquery/jquery.min.js'
              }
          },
          jasmine: {
              options: {
                  destPrefix: 'eucaconsole/static/js/thirdparty/jasmine'
              },
              files: {
                'jasmine_favicon.png': 'jasmine/images/jasmine_favicon.png',
                'jasmine.css': 'jasmine/lib/jasmine-core/jasmine.css',
                'jasmine.js': 'jasmine/lib/jasmine-core/jasmine.js',
                'jasmine-html.js': 'jasmine/lib/jasmine-core/jasmine-html.js',
                'console.js': 'jasmine/lib/console/console.js',
                'boot.js': 'jasmine/lib/jasmine-core/boot/boot.js'
              }
          },
          jasmine_jquery: {
              options: {
                  destPrefix: 'eucaconsole/static/js/thirdparty/jasmine'
              },
              files: {
                'jasmine-jquery.js': 'jasmine-jquery/lib/jasmine-jquery.js'
              }
          },
      },
      jshint: {
          options: {
              reporter: require('jshint-stylish')
          },
          all: ['Gruntfile.js',
                'eucaconsole/static/js/pages/*.js',
                'eucaconsole/static/js/widgets/*.js',
                'eucaconsole/static/js/jasmine-spec/*.js']
      },
      karma: {
          unit: {
              configFile: 'karma.conf.js'
          },
          ci: {
              configFile: 'karma.conf.js',
              singleRun: true,
          }
      },
      clean: {
          min: ["eucaconsole/static/js/minified"],
          production: ["production"]
      },
      copy: {
          production: {
              files: [{ 
                  src: 'eucaconsole/*',
                  dest: 'production/',
              }, {
                  src: 'launcher.sh',
                  dest: 'production/launcher.sh',
              }, {
                  src: 'console.ini',
                  dest: 'production/console.ini',
              }],
              options: {
                  mode: true,
                  timestamp: true
              }
          }
      },
      replace: {
          min: {
              src: ['eucaconsole/templates/*.pt', 'eucaconsole/templates/**/*.pt'],
              overwrite: true,                 
              replacements: [{
                  from: /static\/js\/pages\/(.+)\.js/g,
                  to: 'static/js/minified/pages/$1.min.js'
              }, {
                  from: /static\/js\/widgets\/(.+)\.js/g,
                  to: 'static/js/minified/widgets/$1.min.js' 
              }]             
          },
          nomin: {
              src: ['eucaconsole/templates/*.pt', 'eucaconsole/templates/**/*.pt'],
              overwrite: true,                 
              replacements: [{
                  from: /static\/js\/minified\/pages\/(.+)\.min\.js/g,
                  to: 'static/js/pages/$1.js' 
              }, {
                  from: /static\/js\/minified\/widgets\/(.+)\.min\.js/g,
                  to: 'static/js/widgets/$1.js' 
              }]
          }
      },
      uglify: {
          minify: {
              options: {
                  mangle: false,
                  compress: {
                      drop_console: true
                  }
              },
              files: [
                  {
                      expand: true,     // Enable dynamic expansion.
                      cwd: 'eucaconsole/static/js/',      // Src matches are relative to this path.
                      src: ['pages/*.js', 'widgets/*.js'], // Actual pattern(s) to match.
                      dest: 'eucaconsole/static/js/minified/',   // Destination path prefix.
                      ext: '.min.js',   // Dest filepaths will have this extension.
                      extDot: 'first'   // Extensions in filenames begin after the first dot
                  },
              ]
          }
      },
      watch: {
          scripts: {
              files: ['eucaconsole/static/js/**/*.js'],
              tasks: ['karma:ci', 'jshint'],
              options: {
                  spawn: false,
              },
          },
      }
  });

  // Load the plugins
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-bowercopy');
  grunt.loadNpmTasks('grunt-karma');
  grunt.loadNpmTasks('grunt-text-replace');

  // Default task(s).
  grunt.registerTask('default', ['watch']);
  grunt.registerTask('runtest', ['karma:ci', 'jshint']);
  grunt.registerTask('min', ['uglify', 'replace:min']);
  grunt.registerTask('nomin', ['replace:nomin', 'clean:min']);
  grunt.registerTask('commitcheck', ['runtest', 'nomin']);

};
