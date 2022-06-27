import sys
import pytest
import pandas as pd
import numpy as np

"""
   Signature of functions to test
   def calculate_interval(df, measure, session, top_l_x, top_l_y, bot_r_x, bot_r_y):
   def invert_distribution(prior, likelihood):
   def extract_intervals(dist, intervals, increment):
   def extract_screen_limits(df, bot_r_x, bot_r_y):
   def get_path(n, l_x, l_y, r_x, r_y, exc_l_x=-1,exc_l_y=-1,exc_r_x=-1,exc_r_y=-1):
   def point_inside(temp_x, temp_y, exc_l_x, exc_l_y, exc_r_x, exc_r_y):
   def inside(point, top_l, bot_r):
"""
from gazerr.estimate import invert_distribution
from gazerr.estimate import get_path
from gazerr.estimate import point_inside
from gazerr.estimate import inside
from gazerr.estimate import extract_intervals

def test_pathno_excl():
    mypath = get_path(10, 0, 0, 100, 100)
    assert len(mypath) == 10
    for p in mypath:
        assert p[0] >= 0.0
        assert p[1] >= 0.0
        assert p[0] <= 100.0
        assert p[1] <= 100.0

def test_inside():
    inone = inside((30,30), (20,20), (40,40) )
    outone = inside((0,0), (20,20), (40,40) )
    assert inone == True
    assert outone == False

def test_point_inside():
    inone = point_inside(30,30, 20,20, 40,40 )
    outone = point_inside(0,0, 20,20, 40,40 )
    assert inone == True
    assert outone == False

def test_calculate_interval():
    prior = 0.25
    likelihood = np.array([[0.1,0.1,0.3,0.5],[0.6,0.2,0.1,0.1],[0.2,0.5,0.2,0.1],[0.1,0.1,0.7,0.1]])
    posterior = invert_distribution(prior, likelihood)
    result = extract_intervals(posterior[1,:], [0.95,0.90], increment=100 )
    for r in result.iterrows():
       assert r[1]['Lower'] <= r[1]['Upper']


def test_invert_distribution():
    prior = 0.25
    likelihood = np.array([[0.1,0.1,0.3,0.5],[0.6,0.2,0.1,0.1],[0.2,0.5,0.2,0.1],[0.1,0.1,0.7,0.1]])
    posterior = invert_distribution(prior, likelihood)
    for G in range(len(posterior)):
        total = posterior[G,:].sum()
        assert round(total,6) == 1.0

