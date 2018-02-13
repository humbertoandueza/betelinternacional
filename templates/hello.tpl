{% extends "mail_templated/base.tpl" %}

{% load static %}
{% block subject %}
Hola {{ user.first_name }}
{% endblock %}
{% block body %}
{{ user.ci}}, this is a plain text message.
{% endblock %}

{% block html %}
<style>
	.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
</style>
<div style="margin-top:80px; margin-bottom:80px; margin-left: 180px; height: 250px; width: 400px; border: 1px solid #000; border-radius: 7px; text-align: center; padding: 10px;">
	<br>
	<center>
	<img class="imgr" src="{{lena_image}}" alt="Nosotros" width="200" class="img-fluid my-1 mb-2 " >		
	<h2>Hola {{ user.first_name }}</h2>

	</center>
	<h3>Hemos creado tu usuario, para <strong>completar</strong>  tu inscripción inicia sesión y actualiza tus datos.
</h3>
<br>
<br>
<center>
<a style="color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4; display: inline-block;
  padding: 6px 12px;
  margin-bottom: 0;
  width: 80% !important;
  font-size: 14px;
  font-weight: normal;
  line-height: 1.42857143;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  -ms-touch-action: manipulation;
      touch-action: manipulation;
  cursor: pointer;
  -webkit-user-select: none;
     -moz-user-select: none;
      -ms-user-select: none;
          user-select: none;
  background-image: none;
  border: 1px solid transparent;
  text-decoration: none;
  border-radius: 4px;" class="btn" href="https://iglesiabetel.pythonanywhere.com/accounts/login/">Entrar</a>
</center>
</div>
{% endblock %}