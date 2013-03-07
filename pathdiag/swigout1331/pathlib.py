# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.31
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _pathlib
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


web100_get_Duration = _pathlib.web100_get_Duration
web100_delta_Duration = _pathlib.web100_delta_Duration
web100_get_SndNxt = _pathlib.web100_get_SndNxt
web100_delta_SndNxt = _pathlib.web100_delta_SndNxt
web100_get_SndMax = _pathlib.web100_get_SndMax
web100_delta_SndMax = _pathlib.web100_delta_SndMax
web100_get_SndUna = _pathlib.web100_get_SndUna
web100_delta_SndUna = _pathlib.web100_delta_SndUna
web100_get_CongestionSignals = _pathlib.web100_get_CongestionSignals
web100_delta_CongestionSignals = _pathlib.web100_delta_CongestionSignals
web100_get_PostCongCountRTT = _pathlib.web100_get_PostCongCountRTT
web100_delta_PostCongCountRTT = _pathlib.web100_delta_PostCongCountRTT
web100_get_CurCwnd = _pathlib.web100_get_CurCwnd
web100_get_CurMSS = _pathlib.web100_get_CurMSS
web100_get_TimestampsEnabled = _pathlib.web100_get_TimestampsEnabled
web100_get_SACKEnabled = _pathlib.web100_get_SACKEnabled
web100_get_WinScaleRcvd = _pathlib.web100_get_WinScaleRcvd
web100_get_CountRTT = _pathlib.web100_get_CountRTT
web100_delta_CountRTT = _pathlib.web100_delta_CountRTT
web100_get_SumRTT = _pathlib.web100_get_SumRTT
web100_delta_SumRTT = _pathlib.web100_delta_SumRTT
class web100_readbuf(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, web100_readbuf, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, web100_readbuf, name)
    __repr__ = _swig_repr
    __swig_setmethods__["padding"] = _pathlib.web100_readbuf_padding_set
    __swig_getmethods__["padding"] = _pathlib.web100_readbuf_padding_get
    if _newclass:padding = _swig_property(_pathlib.web100_readbuf_padding_get, _pathlib.web100_readbuf_padding_set)
    def __init__(self, *args): 
        this = _pathlib.new_web100_readbuf(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pathlib.delete_web100_readbuf
    __del__ = lambda self : None;
web100_readbuf_swigregister = _pathlib.web100_readbuf_swigregister
web100_readbuf_swigregister(web100_readbuf)
cvar = _pathlib.cvar

class tctrl(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, tctrl, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, tctrl, name)
    __repr__ = _swig_repr
    __swig_setmethods__["flag"] = _pathlib.tctrl_flag_set
    __swig_getmethods__["flag"] = _pathlib.tctrl_flag_get
    if _newclass:flag = _swig_property(_pathlib.tctrl_flag_get, _pathlib.tctrl_flag_set)
    __swig_setmethods__["basemss"] = _pathlib.tctrl_basemss_set
    __swig_getmethods__["basemss"] = _pathlib.tctrl_basemss_get
    if _newclass:basemss = _swig_property(_pathlib.tctrl_basemss_get, _pathlib.tctrl_basemss_set)
    __swig_setmethods__["win"] = _pathlib.tctrl_win_set
    __swig_getmethods__["win"] = _pathlib.tctrl_win_get
    if _newclass:win = _swig_property(_pathlib.tctrl_win_get, _pathlib.tctrl_win_set)
    __swig_setmethods__["burstwin"] = _pathlib.tctrl_burstwin_set
    __swig_getmethods__["burstwin"] = _pathlib.tctrl_burstwin_get
    if _newclass:burstwin = _swig_property(_pathlib.tctrl_burstwin_get, _pathlib.tctrl_burstwin_set)
    __swig_setmethods__["duration"] = _pathlib.tctrl_duration_set
    __swig_getmethods__["duration"] = _pathlib.tctrl_duration_get
    if _newclass:duration = _swig_property(_pathlib.tctrl_duration_get, _pathlib.tctrl_duration_set)
    __swig_setmethods__["obswin"] = _pathlib.tctrl_obswin_set
    __swig_getmethods__["obswin"] = _pathlib.tctrl_obswin_get
    if _newclass:obswin = _swig_property(_pathlib.tctrl_obswin_get, _pathlib.tctrl_obswin_set)
    __swig_setmethods__["SSbursts"] = _pathlib.tctrl_SSbursts_set
    __swig_getmethods__["SSbursts"] = _pathlib.tctrl_SSbursts_get
    if _newclass:SSbursts = _swig_property(_pathlib.tctrl_SSbursts_get, _pathlib.tctrl_SSbursts_set)
    __swig_setmethods__["SSbully"] = _pathlib.tctrl_SSbully_set
    __swig_getmethods__["SSbully"] = _pathlib.tctrl_SSbully_get
    if _newclass:SSbully = _swig_property(_pathlib.tctrl_SSbully_get, _pathlib.tctrl_SSbully_set)
    __swig_setmethods__["SSbullyStall"] = _pathlib.tctrl_SSbullyStall_set
    __swig_getmethods__["SSbullyStall"] = _pathlib.tctrl_SSbullyStall_get
    if _newclass:SSbullyStall = _swig_property(_pathlib.tctrl_SSbullyStall_get, _pathlib.tctrl_SSbullyStall_set)
    __swig_setmethods__["SSsumAwnd"] = _pathlib.tctrl_SSsumAwnd_set
    __swig_getmethods__["SSsumAwnd"] = _pathlib.tctrl_SSsumAwnd_get
    if _newclass:SSsumAwnd = _swig_property(_pathlib.tctrl_SSsumAwnd_get, _pathlib.tctrl_SSsumAwnd_set)
    __swig_setmethods__["SScntAwnd"] = _pathlib.tctrl_SScntAwnd_set
    __swig_getmethods__["SScntAwnd"] = _pathlib.tctrl_SScntAwnd_get
    if _newclass:SScntAwnd = _swig_property(_pathlib.tctrl_SScntAwnd_get, _pathlib.tctrl_SScntAwnd_set)
    __swig_setmethods__["SSpoll"] = _pathlib.tctrl_SSpoll_set
    __swig_getmethods__["SSpoll"] = _pathlib.tctrl_SSpoll_get
    if _newclass:SSpoll = _swig_property(_pathlib.tctrl_SSpoll_get, _pathlib.tctrl_SSpoll_set)
    def copy(*args): return _pathlib.tctrl_copy(*args)
    def __init__(self, *args): 
        this = _pathlib.new_tctrl(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pathlib.delete_tctrl
    __del__ = lambda self : None;
tctrl_swigregister = _pathlib.tctrl_swigregister
tctrl_swigregister(tctrl)
OneSec = cvar.OneSec

class stats(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, stats, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, stats, name)
    __repr__ = _swig_repr
    __swig_setmethods__["tc"] = _pathlib.stats_tc_set
    __swig_getmethods__["tc"] = _pathlib.stats_tc_get
    if _newclass:tc = _swig_property(_pathlib.stats_tc_get, _pathlib.stats_tc_set)
    __swig_setmethods__["snap"] = _pathlib.stats_snap_set
    __swig_getmethods__["snap"] = _pathlib.stats_snap_get
    if _newclass:snap = _swig_property(_pathlib.stats_snap_get, _pathlib.stats_snap_set)
    def __init__(self, *args): 
        this = _pathlib.new_stats(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pathlib.delete_stats
    __del__ = lambda self : None;
stats_swigregister = _pathlib.stats_swigregister
stats_swigregister(stats)

watch_sample = _pathlib.watch_sample
elapsed_usec = _pathlib.elapsed_usec
stune_conn = _pathlib.stune_conn
watch_elapsed_sample = _pathlib.watch_elapsed_sample
write_web100_var = _pathlib.write_web100_var
pumpsegs = _pathlib.pumpsegs

