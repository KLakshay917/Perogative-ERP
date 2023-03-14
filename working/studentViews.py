from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate ,logout ,login,get_user_model
# from .forms import *
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from datetime import datetime