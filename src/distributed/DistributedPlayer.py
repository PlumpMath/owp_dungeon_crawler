from direct.showbase.DirectObject import DirectObject
from direct.distributed.DistributedSmoothNode import DistributedSmoothNode
from pandac.PandaModules import NodePath

# Distributed Player
class DistributedPlayer(DistributedSmoothNode, DirectObject):
    def __init__(self, cr):
        DistributedSmoothNode.__init__(self, cr)
        NodePath.__init__(self, "Model")
        self.model = base.loader.loadModel('smiley.egg')
        self.model.reparentTo(self)

    def generate(self):
        DistributedSmoothNode.generate(self)
        self.activateSmoothing(True, False)
        self.startSmooth()

    def announceGenerate(self):
        DistributedSmoothNode.announceGenerate(self)
        self.reparentTo(base.render)

    def disable(self):
        self.stopSmooth()
        self.model.detachNode()
        DistributedSmoothNode.disable(self)

    def delete(self):
        self.model = None
        DistributedSmoothNode.delete(self)
