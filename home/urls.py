# coding=utf-8
import views
from django.conf.urls import url
urlpatterns = [
    url(r'^$',views.show_view),
    url(r'^stu/$',views.home_viewx),
    url(r'^a/$',views.a_view),
    url(r'^b/$',views.b_view),
    url(r'^c/$',views.c_view),
    url(r'^d/$',views.d_view),
    url(r'^center/$',views.centera_view),
    # 客户信息
    url(r'^e/$',views.e_view),
    # 客户分配
    url(r'^f/$',views.f_view),
    # 客户关怀
    url(r'^g/$',views.g_view),
    # 客户类型
    url(r'^h/$',views.h_view),
    # 客户状态
    url(r'^i/$',views.i_view),
    # 客户来源
    url(r'j/$',views.j_view),
    # 员工信息
    url(r'^k/$',views.k_view),
    # 房屋信息
    url(r'^l/$',views.l_view),
    # 房屋类型
    url(r'^m/',views.m_view),
    # 部门信息
    url(r'^n/$',views.n_view),
    # 公告
    url(r'^o/$',views.o_view),
    url(r'^p/$',views.p_view),
    url(r'^q/$',views.q_view),
    url(r'^r/$',views.r_view),

]