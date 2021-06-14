# -*- coding: utf-8 -*-
import pathlib
import shutil

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsFeatureRequest,
                       QgsVectorLayer,
                       QgsProject,
                       QgsRasterLayer,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingContext,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterString,
                       QgsProcessingParameterBoolean,
                       QgsProcessingParameterRasterLayer,
                       QgsProcessingParameterVectorLayer,
                       QgsProcessingParameterVectorDestination,
                       QgsProcessingParameterRasterDestination,
                       QgsProcessingLayerPostProcessorInterface,
                       QgsProcessingOutputVectorLayer,
                       QgsProcessingOutputRasterLayer,
                       QgsProcessingParameterFeatureSink)
from qgis import processing

import myMod.myEx as mE

class qgisPart(QgsProcessingAlgorithm):

    DEM = 'DEM'

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return qgisPart()

    def name(self):
        return 'qgisPart'

    def displayName(self):
        return self.tr('qgisPart')

    def group(self):
        return self.tr('AvaFrame')

    def groupId(self):
        return 'avaframe'

    def shortHelpString(self):
        """
        AvaFrame QGis starter
        """
        return self.tr("AvaFrame QGis script")

    def initAlgorithm(self, config=None):

        self.addParameter(QgsProcessingParameterRasterLayer(
            self.DEM,
            self.tr("DEM layer")))

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        sourceDEM = self.parameterAsRasterLayer(parameters, self.DEM, context)
        # if sourceDEM is None:
        #     raise QgsProcessingException(self.invalidSourceError(parameters, self.DEM))

        mE.myMain()


        return {}

# Used to develop together with plugin SCRIPT RUNNER

def run_script(iface):
    print("Script")
    ProfileLayer = ''
    DGMSource = ''
    print('In run script')

