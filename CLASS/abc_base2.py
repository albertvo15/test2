
import abc
import inspect

inspect.getfile(abc.__class__)


class PluginBase(object):
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def load(self,input):
    return

  @abc.abstractmethod
  def save(self,output, data):
    return
