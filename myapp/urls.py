from django.urls import path
from .views import   index_view,about_view,blog_view,ContactView,portfolio_details_view,portfolio_view,single_blog_view

urlpatterns = [
    path('',index_view,name='index-page'),
    path("about/",about_view,name='about-page'),
    path("blog/",blog_view,name='blog-page'),
    path("contact/",ContactView.as_view(),name="contact-page"),
    path("portfolio-details/",portfolio_details_view,name='portfolio-details-page'),
    path("portfolio/",portfolio_view,name='portfolio-page'),
    path("single-blog/",single_blog_view,name='single-blog-page'),

]