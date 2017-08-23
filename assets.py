from django_assets import Bundle, register

main_css = Bundle('scss/base.scss',
            filters='scss, cssmin', output='css/main.min.css')