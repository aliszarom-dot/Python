import pytest
from television import Television

def test_init():
    t = Television()
    assert str(t) == 'Power = False, Channel = 0, Volume =0'
    
def test_power_on():
    t = Television()
    t.power()
    t.power()
    assert str(t) == 'Power = False, Channel = 0, Volume = 0'


def test_mute_on():
    t = Television()
    t.power()
    t.volume_up()
    t.mute()
    assert str(t) == 'Power = True, Channel = 0, Volume = 0'


def test_mute_unmute():
    t = Television()
    t.power()
    t.mute()
    t.mute()
    assert str(t) == 'Power = True, Channel = 0, Volume = 0'
    
def test_mute_tv_off():
    t = Television()
    t.mute()
    assert str(t) == 'Power = False, Channel = 0, Volume = 0'


def test_unmute_tv_off():
    t = Television()
    t.mute()
    t.mute()
    assert str(t) == 'Power = False, Channel = 0, Volume = 0'


def test_channel_up_tv_off():
    t = Television()
    t.channel_up()
    assert str(t) == 'Power = False, Channel = 0, Volume = 0'


def test_channel_up_tv_on():
    t = Television()
    t.power()
    t.channel_up()
    assert str(t) == 'Power = True, Channel = 1, Volume = 0'
    
def test_channel_up_past_max():
    t = Television()
    t.power()
    t.channel_up()
    t.channel_up()
    t.channel_up()
    t.channel_up()
    assert str(t) == 'Power = True, Channel = 0, Volume = 0'


def test_channel_down_tv_off():
    t = Television()
    t.channel_down()
    assert str(t) == 'Power = False, Channel = 0, Volume = 0'


def test_channel_down_past_min():
    t = Television()
    t.power()
    t.channel_down()
    assert str(t) == 'Power = True, Channel = 3, Volume = 0'


def test_volume_up_tv_off():
    t = Television()
    t.volume_up()
    assert str(t) == 'Power = False, Channel = 0, Volume = 0'
    
def test_volume_up_tv_on():
    t = Television()
    t.power()
    t.volume_up()
    assert str(t) == 'Power = True, Channel = 0, Volume = 1'


def test_volume_up_muted():
    t = Television()
    t.power()
    t.mute()
    t.volume_up()
    assert str(t) == 'Power = True, Channel = 0, Volume = 1'


def test_volume_up_past_max():
    t = Television()
    t.power()
    t.volume_up()
    t.volume_up()
    t.volume_up()
    assert str(t) == 'Power = True, Channel = 0, Volume = 2'
    
def test_volume_down_tv_off():
    t = Television()
    t.volume_down()
    assert str(t) == 'Power = False, Channel = 0, Volume = 0'


def test_volume_down_tv_on():
    t = Television()
    t.power()
    t.volume_up()
    t.volume_up()
    t.volume_down()
    assert str(t) == 'Power = True, Channel = 0, Volume = 1'


def test_volume_down_muted():
    t = Television()
    t.power()
    t.mute()
    t.volume_down()
    assert str(t) == 'Power = True, Channel = 0, Volume = 0'


def test_volume_down_past_min():
    t = Television()
    t.power()
    t.volume_down()
    assert str(t) == 'Power = True, Channel = 0, Volume = 0' 