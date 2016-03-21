#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from stupidlang.parser import typer

def test_typer():
    assert typer('true') == True
    assert typer('false') == False
    assert typer('1') == 1
    assert typer('1.1') == 1.1
    assert typer('.1.1') == '.1.1'
    
def test_lex():
    assert lex('()') = [(, )]
    
def test_syn():
    assert syn([(, )]) = []
    
def test_parse():
    assert parse('()') = []
    assert parse('(())') = [[]]
    
print('Running test_parser.py')
print('Testing typer')
test_typer()
print('Testing lex')
test_lex()
print('Testing syn')
test_syn()
print('Testing parse')
test_parse()