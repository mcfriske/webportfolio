from django_assets import Bundle, register

main_css = Bundle('sass/_base.scss', depends="sass/**/*.scss",
            filters='scss, cssmin', output='css/main.min.css')

home_css = Bundle('sass/trumps/home.scss',
             filters='scss, cssmin', output='css/projects/home.min.css')

grid_css = Bundle('sass/trumps/grid.scss',
             filters='scss, cssmin', output='css/projects/grid.min.css')

blog_css = Bundle('sass/trumps/blog.scss',
             filters='scss, cssmin', output='css/projects/blog.min.css')

calendar_css = Bundle('sass/trumps/calendar.scss',
             filters='scss, cssmin', output='css/projects/calendar.min.css')


register('main_css', main_css)
register('grid_css', grid_css)
register('home_css', home_css)
register('blog_css', blog_css)
register('calendar_css', calendar_css)