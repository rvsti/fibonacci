# maintainer: Raj Vardhan Singh

import json, collections
import os, logging
import re, datetime
from django.shortcuts import render_to_response
from django.http import JsonResponse
import utils
import timeit
from functools import partial
import multiprocessing
import time

logger = logging.getLogger( __name__ ) 

def index( request ):
   return render_to_response( 'index.html', {} )


def getValue( request ):
  number = long(request.POST.get( "data" ))
  logger.debug(number)
  que = multiprocessing.Queue()
  p = multiprocessing.Process(target=utils.fibo, name="Fibo", args=(number,que))
  p.start()
  # Wait 1 seconds for fibo
  value = que.get()
  time = value[1]
  value = value[0]
#  print value
  # Terminate after 1 sec
  p.join(100)
  if p.is_alive():
    q.terminate()
  response_data = {}
  response_data['value'] = str(value)
  response_data['time'] = str(time)
  return JsonResponse(response_data)
