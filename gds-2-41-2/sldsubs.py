#!/usr/bin/env python

#
# Generated Wed Mar  1 10:32:35 2023 by generateDS.py version 2.41.2.
# Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)]
#
# Command line options:
#   ('-m', '')
#   ('-f', '')
#   ('-o', 'sld.py')
#   ('-s', 'sldsubs.py')
#
# Command line arguments:
#   StyledLayerDescriptor.xsd
#
# Command line:
#   C:\Users\matthijssenef\git\Test-GenerateDS\venv\Scripts\generateDS.py -m -f -o "sld.py" -s "sldsubs.py" StyledLayerDescriptor.xsd
#
# Current working directory (os.getcwd()):
#   gds-2-41-2
#

import os
import sys
from lxml import etree as etree_

import ??? as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Globals
#

ExternalEncoding = ''
SaveElementTreeNode = True

#
# Data representation classes
#


class StyledLayerDescriptorSub(supermod.StyledLayerDescriptor):
    def __init__(self, version='1.0.0', Name=None, Title=None, Abstract=None, NamedLayer=None, UserLayer=None, **kwargs_):
        super(StyledLayerDescriptorSub, self).__init__(version, Name, Title, Abstract, NamedLayer, UserLayer,  **kwargs_)
supermod.StyledLayerDescriptor.subclass = StyledLayerDescriptorSub
# end class StyledLayerDescriptorSub


class NamedLayerSub(supermod.NamedLayer):
    def __init__(self, Name=None, LayerFeatureConstraints=None, NamedStyle=None, UserStyle=None, **kwargs_):
        super(NamedLayerSub, self).__init__(Name, LayerFeatureConstraints, NamedStyle, UserStyle,  **kwargs_)
supermod.NamedLayer.subclass = NamedLayerSub
# end class NamedLayerSub


class NamedStyleSub(supermod.NamedStyle):
    def __init__(self, Name=None, **kwargs_):
        super(NamedStyleSub, self).__init__(Name,  **kwargs_)
supermod.NamedStyle.subclass = NamedStyleSub
# end class NamedStyleSub


class UserLayerSub(supermod.UserLayer):
    def __init__(self, Name=None, RemoteOWS=None, LayerFeatureConstraints=None, UserStyle=None, **kwargs_):
        super(UserLayerSub, self).__init__(Name, RemoteOWS, LayerFeatureConstraints, UserStyle,  **kwargs_)
supermod.UserLayer.subclass = UserLayerSub
# end class UserLayerSub


class RemoteOWSSub(supermod.RemoteOWS):
    def __init__(self, Service=None, OnlineResource=None, **kwargs_):
        super(RemoteOWSSub, self).__init__(Service, OnlineResource,  **kwargs_)
supermod.RemoteOWS.subclass = RemoteOWSSub
# end class RemoteOWSSub


class OnlineResourceSub(supermod.OnlineResource):
    def __init__(self, type_='simple', href=None, role=None, arcrole=None, title=None, show=None, actuate=None, **kwargs_):
        super(OnlineResourceSub, self).__init__(type_, href, role, arcrole, title, show, actuate,  **kwargs_)
supermod.OnlineResource.subclass = OnlineResourceSub
# end class OnlineResourceSub


class LayerFeatureConstraintsSub(supermod.LayerFeatureConstraints):
    def __init__(self, FeatureTypeConstraint=None, **kwargs_):
        super(LayerFeatureConstraintsSub, self).__init__(FeatureTypeConstraint,  **kwargs_)
supermod.LayerFeatureConstraints.subclass = LayerFeatureConstraintsSub
# end class LayerFeatureConstraintsSub


class FeatureTypeConstraintSub(supermod.FeatureTypeConstraint):
    def __init__(self, FeatureTypeName=None, Filter=None, Extent=None, **kwargs_):
        super(FeatureTypeConstraintSub, self).__init__(FeatureTypeName, Filter, Extent,  **kwargs_)
supermod.FeatureTypeConstraint.subclass = FeatureTypeConstraintSub
# end class FeatureTypeConstraintSub


class ExtentSub(supermod.Extent):
    def __init__(self, Name=None, Value=None, **kwargs_):
        super(ExtentSub, self).__init__(Name, Value,  **kwargs_)
supermod.Extent.subclass = ExtentSub
# end class ExtentSub


class UserStyleSub(supermod.UserStyle):
    def __init__(self, Name=None, Title=None, Abstract=None, IsDefault=None, FeatureTypeStyle=None, **kwargs_):
        super(UserStyleSub, self).__init__(Name, Title, Abstract, IsDefault, FeatureTypeStyle,  **kwargs_)
supermod.UserStyle.subclass = UserStyleSub
# end class UserStyleSub


class FeatureTypeStyleSub(supermod.FeatureTypeStyle):
    def __init__(self, Name=None, Title=None, Abstract=None, FeatureTypeName=None, SemanticTypeIdentifier=None, Rule=None, **kwargs_):
        super(FeatureTypeStyleSub, self).__init__(Name, Title, Abstract, FeatureTypeName, SemanticTypeIdentifier, Rule,  **kwargs_)
supermod.FeatureTypeStyle.subclass = FeatureTypeStyleSub
# end class FeatureTypeStyleSub


class RuleSub(supermod.Rule):
    def __init__(self, Name=None, Title=None, Abstract=None, LegendGraphic=None, Filter=None, ElseFilter=None, MinScaleDenominator=None, MaxScaleDenominator=None, Symbolizer=None, **kwargs_):
        super(RuleSub, self).__init__(Name, Title, Abstract, LegendGraphic, Filter, ElseFilter, MinScaleDenominator, MaxScaleDenominator, Symbolizer,  **kwargs_)
supermod.Rule.subclass = RuleSub
# end class RuleSub


class LegendGraphicSub(supermod.LegendGraphic):
    def __init__(self, Graphic=None, **kwargs_):
        super(LegendGraphicSub, self).__init__(Graphic,  **kwargs_)
supermod.LegendGraphic.subclass = LegendGraphicSub
# end class LegendGraphicSub


class ElseFilterSub(supermod.ElseFilter):
    def __init__(self, **kwargs_):
        super(ElseFilterSub, self).__init__( **kwargs_)
supermod.ElseFilter.subclass = ElseFilterSub
# end class ElseFilterSub


class SymbolizerTypeSub(supermod.SymbolizerType):
    def __init__(self, extensiontype_=None, **kwargs_):
        super(SymbolizerTypeSub, self).__init__(extensiontype_,  **kwargs_)
supermod.SymbolizerType.subclass = SymbolizerTypeSub
# end class SymbolizerTypeSub


class LineSymbolizerSub(supermod.LineSymbolizer):
    def __init__(self, Geometry=None, Stroke=None, **kwargs_):
        super(LineSymbolizerSub, self).__init__(Geometry, Stroke,  **kwargs_)
supermod.LineSymbolizer.subclass = LineSymbolizerSub
# end class LineSymbolizerSub


class GeometrySub(supermod.Geometry):
    def __init__(self, PropertyName=None, **kwargs_):
        super(GeometrySub, self).__init__(PropertyName,  **kwargs_)
supermod.Geometry.subclass = GeometrySub
# end class GeometrySub


class StrokeSub(supermod.Stroke):
    def __init__(self, GraphicFill=None, GraphicStroke=None, CssParameter=None, **kwargs_):
        super(StrokeSub, self).__init__(GraphicFill, GraphicStroke, CssParameter,  **kwargs_)
supermod.Stroke.subclass = StrokeSub
# end class StrokeSub


class ParameterValueTypeSub(supermod.ParameterValueType):
    def __init__(self, expression=None, valueOf_=None, mixedclass_=None, content_=None, extensiontype_=None, **kwargs_):
        super(ParameterValueTypeSub, self).__init__(expression, valueOf_, mixedclass_, content_, extensiontype_,  **kwargs_)
supermod.ParameterValueType.subclass = ParameterValueTypeSub
# end class ParameterValueTypeSub


class GraphicFillSub(supermod.GraphicFill):
    def __init__(self, Graphic=None, **kwargs_):
        super(GraphicFillSub, self).__init__(Graphic,  **kwargs_)
supermod.GraphicFill.subclass = GraphicFillSub
# end class GraphicFillSub


class GraphicStrokeSub(supermod.GraphicStroke):
    def __init__(self, Graphic=None, **kwargs_):
        super(GraphicStrokeSub, self).__init__(Graphic,  **kwargs_)
supermod.GraphicStroke.subclass = GraphicStrokeSub
# end class GraphicStrokeSub


class PolygonSymbolizerSub(supermod.PolygonSymbolizer):
    def __init__(self, Geometry=None, Fill=None, Stroke=None, **kwargs_):
        super(PolygonSymbolizerSub, self).__init__(Geometry, Fill, Stroke,  **kwargs_)
supermod.PolygonSymbolizer.subclass = PolygonSymbolizerSub
# end class PolygonSymbolizerSub


class FillSub(supermod.Fill):
    def __init__(self, GraphicFill=None, CssParameter=None, **kwargs_):
        super(FillSub, self).__init__(GraphicFill, CssParameter,  **kwargs_)
supermod.Fill.subclass = FillSub
# end class FillSub


class PointSymbolizerSub(supermod.PointSymbolizer):
    def __init__(self, Geometry=None, Graphic=None, **kwargs_):
        super(PointSymbolizerSub, self).__init__(Geometry, Graphic,  **kwargs_)
supermod.PointSymbolizer.subclass = PointSymbolizerSub
# end class PointSymbolizerSub


class GraphicSub(supermod.Graphic):
    def __init__(self, ExternalGraphic=None, Mark=None, Opacity=None, Size=None, Rotation=None, **kwargs_):
        super(GraphicSub, self).__init__(ExternalGraphic, Mark, Opacity, Size, Rotation,  **kwargs_)
supermod.Graphic.subclass = GraphicSub
# end class GraphicSub


class ExternalGraphicSub(supermod.ExternalGraphic):
    def __init__(self, OnlineResource=None, Format=None, **kwargs_):
        super(ExternalGraphicSub, self).__init__(OnlineResource, Format,  **kwargs_)
supermod.ExternalGraphic.subclass = ExternalGraphicSub
# end class ExternalGraphicSub


class MarkSub(supermod.Mark):
    def __init__(self, WellKnownName=None, Fill=None, Stroke=None, **kwargs_):
        super(MarkSub, self).__init__(WellKnownName, Fill, Stroke,  **kwargs_)
supermod.Mark.subclass = MarkSub
# end class MarkSub


class TextSymbolizerSub(supermod.TextSymbolizer):
    def __init__(self, Geometry=None, Label=None, Font=None, LabelPlacement=None, Halo=None, Fill=None, **kwargs_):
        super(TextSymbolizerSub, self).__init__(Geometry, Label, Font, LabelPlacement, Halo, Fill,  **kwargs_)
supermod.TextSymbolizer.subclass = TextSymbolizerSub
# end class TextSymbolizerSub


class FontSub(supermod.Font):
    def __init__(self, CssParameter=None, **kwargs_):
        super(FontSub, self).__init__(CssParameter,  **kwargs_)
supermod.Font.subclass = FontSub
# end class FontSub


class LabelPlacementSub(supermod.LabelPlacement):
    def __init__(self, PointPlacement=None, LinePlacement=None, **kwargs_):
        super(LabelPlacementSub, self).__init__(PointPlacement, LinePlacement,  **kwargs_)
supermod.LabelPlacement.subclass = LabelPlacementSub
# end class LabelPlacementSub


class PointPlacementSub(supermod.PointPlacement):
    def __init__(self, AnchorPoint=None, Displacement=None, Rotation=None, **kwargs_):
        super(PointPlacementSub, self).__init__(AnchorPoint, Displacement, Rotation,  **kwargs_)
supermod.PointPlacement.subclass = PointPlacementSub
# end class PointPlacementSub


class AnchorPointSub(supermod.AnchorPoint):
    def __init__(self, AnchorPointX=None, AnchorPointY=None, **kwargs_):
        super(AnchorPointSub, self).__init__(AnchorPointX, AnchorPointY,  **kwargs_)
supermod.AnchorPoint.subclass = AnchorPointSub
# end class AnchorPointSub


class DisplacementSub(supermod.Displacement):
    def __init__(self, DisplacementX=None, DisplacementY=None, **kwargs_):
        super(DisplacementSub, self).__init__(DisplacementX, DisplacementY,  **kwargs_)
supermod.Displacement.subclass = DisplacementSub
# end class DisplacementSub


class LinePlacementSub(supermod.LinePlacement):
    def __init__(self, PerpendicularOffset=None, **kwargs_):
        super(LinePlacementSub, self).__init__(PerpendicularOffset,  **kwargs_)
supermod.LinePlacement.subclass = LinePlacementSub
# end class LinePlacementSub


class HaloSub(supermod.Halo):
    def __init__(self, Radius=None, Fill=None, **kwargs_):
        super(HaloSub, self).__init__(Radius, Fill,  **kwargs_)
supermod.Halo.subclass = HaloSub
# end class HaloSub


class RasterSymbolizerSub(supermod.RasterSymbolizer):
    def __init__(self, Geometry=None, Opacity=None, ChannelSelection=None, OverlapBehavior=None, ColorMap=None, ContrastEnhancement=None, ShadedRelief=None, ImageOutline=None, **kwargs_):
        super(RasterSymbolizerSub, self).__init__(Geometry, Opacity, ChannelSelection, OverlapBehavior, ColorMap, ContrastEnhancement, ShadedRelief, ImageOutline,  **kwargs_)
supermod.RasterSymbolizer.subclass = RasterSymbolizerSub
# end class RasterSymbolizerSub


class ChannelSelectionSub(supermod.ChannelSelection):
    def __init__(self, RedChannel=None, GreenChannel=None, BlueChannel=None, GrayChannel=None, **kwargs_):
        super(ChannelSelectionSub, self).__init__(RedChannel, GreenChannel, BlueChannel, GrayChannel,  **kwargs_)
supermod.ChannelSelection.subclass = ChannelSelectionSub
# end class ChannelSelectionSub


class SelectedChannelTypeSub(supermod.SelectedChannelType):
    def __init__(self, SourceChannelName=None, ContrastEnhancement=None, **kwargs_):
        super(SelectedChannelTypeSub, self).__init__(SourceChannelName, ContrastEnhancement,  **kwargs_)
supermod.SelectedChannelType.subclass = SelectedChannelTypeSub
# end class SelectedChannelTypeSub


class OverlapBehaviorSub(supermod.OverlapBehavior):
    def __init__(self, LATEST_ON_TOP=None, EARLIEST_ON_TOP=None, AVERAGE=None, RANDOM=None, **kwargs_):
        super(OverlapBehaviorSub, self).__init__(LATEST_ON_TOP, EARLIEST_ON_TOP, AVERAGE, RANDOM,  **kwargs_)
supermod.OverlapBehavior.subclass = OverlapBehaviorSub
# end class OverlapBehaviorSub


class LATEST_ON_TOPSub(supermod.LATEST_ON_TOP):
    def __init__(self, **kwargs_):
        super(LATEST_ON_TOPSub, self).__init__( **kwargs_)
supermod.LATEST_ON_TOP.subclass = LATEST_ON_TOPSub
# end class LATEST_ON_TOPSub


class EARLIEST_ON_TOPSub(supermod.EARLIEST_ON_TOP):
    def __init__(self, **kwargs_):
        super(EARLIEST_ON_TOPSub, self).__init__( **kwargs_)
supermod.EARLIEST_ON_TOP.subclass = EARLIEST_ON_TOPSub
# end class EARLIEST_ON_TOPSub


class AVERAGESub(supermod.AVERAGE):
    def __init__(self, **kwargs_):
        super(AVERAGESub, self).__init__( **kwargs_)
supermod.AVERAGE.subclass = AVERAGESub
# end class AVERAGESub


class RANDOMSub(supermod.RANDOM):
    def __init__(self, **kwargs_):
        super(RANDOMSub, self).__init__( **kwargs_)
supermod.RANDOM.subclass = RANDOMSub
# end class RANDOMSub


class ColorMapSub(supermod.ColorMap):
    def __init__(self, ColorMapEntry=None, **kwargs_):
        super(ColorMapSub, self).__init__(ColorMapEntry,  **kwargs_)
supermod.ColorMap.subclass = ColorMapSub
# end class ColorMapSub


class ColorMapEntrySub(supermod.ColorMapEntry):
    def __init__(self, color=None, opacity=None, quantity=None, label=None, **kwargs_):
        super(ColorMapEntrySub, self).__init__(color, opacity, quantity, label,  **kwargs_)
supermod.ColorMapEntry.subclass = ColorMapEntrySub
# end class ColorMapEntrySub


class ContrastEnhancementSub(supermod.ContrastEnhancement):
    def __init__(self, Normalize=None, Histogram=None, GammaValue=None, **kwargs_):
        super(ContrastEnhancementSub, self).__init__(Normalize, Histogram, GammaValue,  **kwargs_)
supermod.ContrastEnhancement.subclass = ContrastEnhancementSub
# end class ContrastEnhancementSub


class NormalizeSub(supermod.Normalize):
    def __init__(self, **kwargs_):
        super(NormalizeSub, self).__init__( **kwargs_)
supermod.Normalize.subclass = NormalizeSub
# end class NormalizeSub


class HistogramSub(supermod.Histogram):
    def __init__(self, **kwargs_):
        super(HistogramSub, self).__init__( **kwargs_)
supermod.Histogram.subclass = HistogramSub
# end class HistogramSub


class ShadedReliefSub(supermod.ShadedRelief):
    def __init__(self, BrightnessOnly=None, ReliefFactor=None, **kwargs_):
        super(ShadedReliefSub, self).__init__(BrightnessOnly, ReliefFactor,  **kwargs_)
supermod.ShadedRelief.subclass = ShadedReliefSub
# end class ShadedReliefSub


class ImageOutlineSub(supermod.ImageOutline):
    def __init__(self, LineSymbolizer=None, PolygonSymbolizer=None, **kwargs_):
        super(ImageOutlineSub, self).__init__(LineSymbolizer, PolygonSymbolizer,  **kwargs_)
supermod.ImageOutline.subclass = ImageOutlineSub
# end class ImageOutlineSub


class simpleSub(supermod.simple):
    def __init__(self, type_='simple', href=None, role=None, arcrole=None, title=None, show=None, actuate=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(simpleSub, self).__init__(type_, href, role, arcrole, title, show, actuate, anytypeobjs_, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.simple.subclass = simpleSub
# end class simpleSub


class extendedSub(supermod.extended):
    def __init__(self, type_='extended', role=None, title_attr=None, title=None, resource=None, locator=None, arc=None, **kwargs_):
        super(extendedSub, self).__init__(type_, role, title_attr, title, resource, locator, arc,  **kwargs_)
supermod.extended.subclass = extendedSub
# end class extendedSub


class titleEltTypeSub(supermod.titleEltType):
    def __init__(self, type_='title', lang=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(titleEltTypeSub, self).__init__(type_, lang, anytypeobjs_, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.titleEltType.subclass = titleEltTypeSub
# end class titleEltTypeSub


class resourceTypeSub(supermod.resourceType):
    def __init__(self, type_='resource', role=None, title=None, label=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(resourceTypeSub, self).__init__(type_, role, title, label, anytypeobjs_, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.resourceType.subclass = resourceTypeSub
# end class resourceTypeSub


class locatorTypeSub(supermod.locatorType):
    def __init__(self, type_='locator', href=None, role=None, title_attr=None, label=None, title=None, **kwargs_):
        super(locatorTypeSub, self).__init__(type_, href, role, title_attr, label, title,  **kwargs_)
supermod.locatorType.subclass = locatorTypeSub
# end class locatorTypeSub


class arcTypeSub(supermod.arcType):
    def __init__(self, type_='arc', arcrole=None, title_attr=None, show=None, actuate=None, from_=None, to=None, title=None, **kwargs_):
        super(arcTypeSub, self).__init__(type_, arcrole, title_attr, show, actuate, from_, to, title,  **kwargs_)
supermod.arcType.subclass = arcTypeSub
# end class arcTypeSub


class ComparisonOpsTypeSub(supermod.ComparisonOpsType):
    def __init__(self, extensiontype_=None, **kwargs_):
        super(ComparisonOpsTypeSub, self).__init__(extensiontype_,  **kwargs_)
supermod.ComparisonOpsType.subclass = ComparisonOpsTypeSub
# end class ComparisonOpsTypeSub


class SpatialOpsTypeSub(supermod.SpatialOpsType):
    def __init__(self, extensiontype_=None, **kwargs_):
        super(SpatialOpsTypeSub, self).__init__(extensiontype_,  **kwargs_)
supermod.SpatialOpsType.subclass = SpatialOpsTypeSub
# end class SpatialOpsTypeSub


class LogicOpsTypeSub(supermod.LogicOpsType):
    def __init__(self, extensiontype_=None, **kwargs_):
        super(LogicOpsTypeSub, self).__init__(extensiontype_,  **kwargs_)
supermod.LogicOpsType.subclass = LogicOpsTypeSub
# end class LogicOpsTypeSub


class FilterTypeSub(supermod.FilterType):
    def __init__(self, spatialOps=None, comparisonOps=None, logicOps=None, FeatureId=None, **kwargs_):
        super(FilterTypeSub, self).__init__(spatialOps, comparisonOps, logicOps, FeatureId,  **kwargs_)
supermod.FilterType.subclass = FilterTypeSub
# end class FilterTypeSub


class FeatureIdTypeSub(supermod.FeatureIdType):
    def __init__(self, fid=None, **kwargs_):
        super(FeatureIdTypeSub, self).__init__(fid,  **kwargs_)
supermod.FeatureIdType.subclass = FeatureIdTypeSub
# end class FeatureIdTypeSub


class BinaryComparisonOpTypeSub(supermod.BinaryComparisonOpType):
    def __init__(self, expression=None, **kwargs_):
        super(BinaryComparisonOpTypeSub, self).__init__(expression,  **kwargs_)
supermod.BinaryComparisonOpType.subclass = BinaryComparisonOpTypeSub
# end class BinaryComparisonOpTypeSub


class PropertyIsLikeTypeSub(supermod.PropertyIsLikeType):
    def __init__(self, wildCard=None, singleChar=None, escape=None, PropertyName=None, Literal=None, **kwargs_):
        super(PropertyIsLikeTypeSub, self).__init__(wildCard, singleChar, escape, PropertyName, Literal,  **kwargs_)
supermod.PropertyIsLikeType.subclass = PropertyIsLikeTypeSub
# end class PropertyIsLikeTypeSub


class PropertyIsNullTypeSub(supermod.PropertyIsNullType):
    def __init__(self, PropertyName=None, Literal=None, **kwargs_):
        super(PropertyIsNullTypeSub, self).__init__(PropertyName, Literal,  **kwargs_)
supermod.PropertyIsNullType.subclass = PropertyIsNullTypeSub
# end class PropertyIsNullTypeSub


class PropertyIsBetweenTypeSub(supermod.PropertyIsBetweenType):
    def __init__(self, expression=None, LowerBoundary=None, UpperBoundary=None, **kwargs_):
        super(PropertyIsBetweenTypeSub, self).__init__(expression, LowerBoundary, UpperBoundary,  **kwargs_)
supermod.PropertyIsBetweenType.subclass = PropertyIsBetweenTypeSub
# end class PropertyIsBetweenTypeSub


class LowerBoundaryTypeSub(supermod.LowerBoundaryType):
    def __init__(self, expression=None, **kwargs_):
        super(LowerBoundaryTypeSub, self).__init__(expression,  **kwargs_)
supermod.LowerBoundaryType.subclass = LowerBoundaryTypeSub
# end class LowerBoundaryTypeSub


class UpperBoundaryTypeSub(supermod.UpperBoundaryType):
    def __init__(self, expression=None, **kwargs_):
        super(UpperBoundaryTypeSub, self).__init__(expression,  **kwargs_)
supermod.UpperBoundaryType.subclass = UpperBoundaryTypeSub
# end class UpperBoundaryTypeSub


class BinarySpatialOpTypeSub(supermod.BinarySpatialOpType):
    def __init__(self, PropertyName=None, _Geometry=None, Box=None, **kwargs_):
        super(BinarySpatialOpTypeSub, self).__init__(PropertyName, _Geometry, Box,  **kwargs_)
supermod.BinarySpatialOpType.subclass = BinarySpatialOpTypeSub
# end class BinarySpatialOpTypeSub


class BBOXTypeSub(supermod.BBOXType):
    def __init__(self, PropertyName=None, Box=None, **kwargs_):
        super(BBOXTypeSub, self).__init__(PropertyName, Box,  **kwargs_)
supermod.BBOXType.subclass = BBOXTypeSub
# end class BBOXTypeSub


class DistanceBufferTypeSub(supermod.DistanceBufferType):
    def __init__(self, PropertyName=None, _Geometry=None, Distance=None, **kwargs_):
        super(DistanceBufferTypeSub, self).__init__(PropertyName, _Geometry, Distance,  **kwargs_)
supermod.DistanceBufferType.subclass = DistanceBufferTypeSub
# end class DistanceBufferTypeSub


class DistanceTypeSub(supermod.DistanceType):
    def __init__(self, units=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(DistanceTypeSub, self).__init__(units, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.DistanceType.subclass = DistanceTypeSub
# end class DistanceTypeSub


class BinaryLogicOpTypeSub(supermod.BinaryLogicOpType):
    def __init__(self, comparisonOps=None, spatialOps=None, logicOps=None, **kwargs_):
        super(BinaryLogicOpTypeSub, self).__init__(comparisonOps, spatialOps, logicOps,  **kwargs_)
supermod.BinaryLogicOpType.subclass = BinaryLogicOpTypeSub
# end class BinaryLogicOpTypeSub


class UnaryLogicOpTypeSub(supermod.UnaryLogicOpType):
    def __init__(self, comparisonOps=None, spatialOps=None, logicOps=None, **kwargs_):
        super(UnaryLogicOpTypeSub, self).__init__(comparisonOps, spatialOps, logicOps,  **kwargs_)
supermod.UnaryLogicOpType.subclass = UnaryLogicOpTypeSub
# end class UnaryLogicOpTypeSub


class ExpressionTypeSub(supermod.ExpressionType):
    def __init__(self, extensiontype_=None, **kwargs_):
        super(ExpressionTypeSub, self).__init__(extensiontype_,  **kwargs_)
supermod.ExpressionType.subclass = ExpressionTypeSub
# end class ExpressionTypeSub


class BinaryOperatorTypeSub(supermod.BinaryOperatorType):
    def __init__(self, expression=None, **kwargs_):
        super(BinaryOperatorTypeSub, self).__init__(expression,  **kwargs_)
supermod.BinaryOperatorType.subclass = BinaryOperatorTypeSub
# end class BinaryOperatorTypeSub


class FunctionTypeSub(supermod.FunctionType):
    def __init__(self, name=None, expression=None, **kwargs_):
        super(FunctionTypeSub, self).__init__(name, expression,  **kwargs_)
supermod.FunctionType.subclass = FunctionTypeSub
# end class FunctionTypeSub


class LiteralTypeSub(supermod.LiteralType):
    def __init__(self, anytypeobjs_=None, **kwargs_):
        super(LiteralTypeSub, self).__init__(anytypeobjs_,  **kwargs_)
supermod.LiteralType.subclass = LiteralTypeSub
# end class LiteralTypeSub


class PropertyNameTypeSub(supermod.PropertyNameType):
    def __init__(self, **kwargs_):
        super(PropertyNameTypeSub, self).__init__( **kwargs_)
supermod.PropertyNameType.subclass = PropertyNameTypeSub
# end class PropertyNameTypeSub


class AbstractGeometryTypeSub(supermod.AbstractGeometryType):
    def __init__(self, gid=None, srsName=None, extensiontype_=None, **kwargs_):
        super(AbstractGeometryTypeSub, self).__init__(gid, srsName, extensiontype_,  **kwargs_)
supermod.AbstractGeometryType.subclass = AbstractGeometryTypeSub
# end class AbstractGeometryTypeSub


class AbstractGeometryCollectionBaseTypeSub(supermod.AbstractGeometryCollectionBaseType):
    def __init__(self, gid=None, srsName=None, extensiontype_=None, **kwargs_):
        super(AbstractGeometryCollectionBaseTypeSub, self).__init__(gid, srsName, extensiontype_,  **kwargs_)
supermod.AbstractGeometryCollectionBaseType.subclass = AbstractGeometryCollectionBaseTypeSub
# end class AbstractGeometryCollectionBaseTypeSub


class GeometryAssociationTypeSub(supermod.GeometryAssociationType):
    def __init__(self, remoteSchema=None, type_='simple', href=None, role=None, arcrole=None, title=None, show=None, actuate=None, _Geometry=None, **kwargs_):
        super(GeometryAssociationTypeSub, self).__init__(remoteSchema, type_, href, role, arcrole, title, show, actuate, _Geometry,  **kwargs_)
supermod.GeometryAssociationType.subclass = GeometryAssociationTypeSub
# end class GeometryAssociationTypeSub


class PointMemberTypeSub(supermod.PointMemberType):
    def __init__(self, type_='simple', href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, Point=None, **kwargs_):
        super(PointMemberTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, Point,  **kwargs_)
supermod.PointMemberType.subclass = PointMemberTypeSub
# end class PointMemberTypeSub


class LineStringMemberTypeSub(supermod.LineStringMemberType):
    def __init__(self, type_='simple', href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, LineString=None, **kwargs_):
        super(LineStringMemberTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, LineString,  **kwargs_)
supermod.LineStringMemberType.subclass = LineStringMemberTypeSub
# end class LineStringMemberTypeSub


class PolygonMemberTypeSub(supermod.PolygonMemberType):
    def __init__(self, type_='simple', href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, Polygon=None, **kwargs_):
        super(PolygonMemberTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, Polygon,  **kwargs_)
supermod.PolygonMemberType.subclass = PolygonMemberTypeSub
# end class PolygonMemberTypeSub


class LinearRingMemberTypeSub(supermod.LinearRingMemberType):
    def __init__(self, type_='simple', href=None, role=None, arcrole=None, title=None, show=None, actuate=None, remoteSchema=None, LinearRing=None, **kwargs_):
        super(LinearRingMemberTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, remoteSchema, LinearRing,  **kwargs_)
supermod.LinearRingMemberType.subclass = LinearRingMemberTypeSub
# end class LinearRingMemberTypeSub


class PointTypeSub(supermod.PointType):
    def __init__(self, gid=None, srsName=None, coord=None, coordinates=None, **kwargs_):
        super(PointTypeSub, self).__init__(gid, srsName, coord, coordinates,  **kwargs_)
supermod.PointType.subclass = PointTypeSub
# end class PointTypeSub


class LineStringTypeSub(supermod.LineStringType):
    def __init__(self, gid=None, srsName=None, coord=None, coordinates=None, **kwargs_):
        super(LineStringTypeSub, self).__init__(gid, srsName, coord, coordinates,  **kwargs_)
supermod.LineStringType.subclass = LineStringTypeSub
# end class LineStringTypeSub


class LinearRingTypeSub(supermod.LinearRingType):
    def __init__(self, gid=None, srsName=None, coord=None, coordinates=None, **kwargs_):
        super(LinearRingTypeSub, self).__init__(gid, srsName, coord, coordinates,  **kwargs_)
supermod.LinearRingType.subclass = LinearRingTypeSub
# end class LinearRingTypeSub


class BoxTypeSub(supermod.BoxType):
    def __init__(self, gid=None, srsName=None, coord=None, coordinates=None, **kwargs_):
        super(BoxTypeSub, self).__init__(gid, srsName, coord, coordinates,  **kwargs_)
supermod.BoxType.subclass = BoxTypeSub
# end class BoxTypeSub


class PolygonTypeSub(supermod.PolygonType):
    def __init__(self, gid=None, srsName=None, outerBoundaryIs=None, innerBoundaryIs=None, **kwargs_):
        super(PolygonTypeSub, self).__init__(gid, srsName, outerBoundaryIs, innerBoundaryIs,  **kwargs_)
supermod.PolygonType.subclass = PolygonTypeSub
# end class PolygonTypeSub


class GeometryCollectionTypeSub(supermod.GeometryCollectionType):
    def __init__(self, gid=None, srsName=None, geometryMember=None, **kwargs_):
        super(GeometryCollectionTypeSub, self).__init__(gid, srsName, geometryMember,  **kwargs_)
supermod.GeometryCollectionType.subclass = GeometryCollectionTypeSub
# end class GeometryCollectionTypeSub


class MultiPointTypeSub(supermod.MultiPointType):
    def __init__(self, gid=None, srsName=None, pointMember=None, **kwargs_):
        super(MultiPointTypeSub, self).__init__(gid, srsName, pointMember,  **kwargs_)
supermod.MultiPointType.subclass = MultiPointTypeSub
# end class MultiPointTypeSub


class MultiLineStringTypeSub(supermod.MultiLineStringType):
    def __init__(self, gid=None, srsName=None, lineStringMember=None, **kwargs_):
        super(MultiLineStringTypeSub, self).__init__(gid, srsName, lineStringMember,  **kwargs_)
supermod.MultiLineStringType.subclass = MultiLineStringTypeSub
# end class MultiLineStringTypeSub


class MultiPolygonTypeSub(supermod.MultiPolygonType):
    def __init__(self, gid=None, srsName=None, polygonMember=None, **kwargs_):
        super(MultiPolygonTypeSub, self).__init__(gid, srsName, polygonMember,  **kwargs_)
supermod.MultiPolygonType.subclass = MultiPolygonTypeSub
# end class MultiPolygonTypeSub


class CoordTypeSub(supermod.CoordType):
    def __init__(self, X=None, Y=None, Z=None, **kwargs_):
        super(CoordTypeSub, self).__init__(X, Y, Z,  **kwargs_)
supermod.CoordType.subclass = CoordTypeSub
# end class CoordTypeSub


class CoordinatesTypeSub(supermod.CoordinatesType):
    def __init__(self, decimal='.', cs=',', ts=' ', valueOf_=None, **kwargs_):
        super(CoordinatesTypeSub, self).__init__(decimal, cs, ts, valueOf_,  **kwargs_)
supermod.CoordinatesType.subclass = CoordinatesTypeSub
# end class CoordinatesTypeSub


class AbstractFeatureTypeSub(supermod.AbstractFeatureType):
    def __init__(self, fid=None, description=None, name=None, boundedBy=None, **kwargs_):
        super(AbstractFeatureTypeSub, self).__init__(fid, description, name, boundedBy,  **kwargs_)
supermod.AbstractFeatureType.subclass = AbstractFeatureTypeSub
# end class AbstractFeatureTypeSub


class AbstractFeatureCollectionBaseTypeSub(supermod.AbstractFeatureCollectionBaseType):
    def __init__(self, fid=None, description=None, name=None, boundedBy=None, extensiontype_=None, **kwargs_):
        super(AbstractFeatureCollectionBaseTypeSub, self).__init__(fid, description, name, boundedBy, extensiontype_,  **kwargs_)
supermod.AbstractFeatureCollectionBaseType.subclass = AbstractFeatureCollectionBaseTypeSub
# end class AbstractFeatureCollectionBaseTypeSub


class AbstractFeatureCollectionTypeSub(supermod.AbstractFeatureCollectionType):
    def __init__(self, fid=None, description=None, name=None, boundedBy=None, featureMember=None, **kwargs_):
        super(AbstractFeatureCollectionTypeSub, self).__init__(fid, description, name, boundedBy, featureMember,  **kwargs_)
supermod.AbstractFeatureCollectionType.subclass = AbstractFeatureCollectionTypeSub
# end class AbstractFeatureCollectionTypeSub


class GeometryPropertyTypeSub(supermod.GeometryPropertyType):
    def __init__(self, remoteSchema=None, type_='simple', href=None, role=None, arcrole=None, title=None, show=None, actuate=None, _Geometry=None, **kwargs_):
        super(GeometryPropertyTypeSub, self).__init__(remoteSchema, type_, href, role, arcrole, title, show, actuate, _Geometry,  **kwargs_)
supermod.GeometryPropertyType.subclass = GeometryPropertyTypeSub
# end class GeometryPropertyTypeSub


class FeatureAssociationTypeSub(supermod.FeatureAssociationType):
    def __init__(self, remoteSchema=None, type_='simple', href=None, role=None, arcrole=None, title=None, show=None, actuate=None, _Feature=None, **kwargs_):
        super(FeatureAssociationTypeSub, self).__init__(remoteSchema, type_, href, role, arcrole, title, show, actuate, _Feature,  **kwargs_)
supermod.FeatureAssociationType.subclass = FeatureAssociationTypeSub
# end class FeatureAssociationTypeSub


class BoundingShapeTypeSub(supermod.BoundingShapeType):
    def __init__(self, Box=None, null=None, **kwargs_):
        super(BoundingShapeTypeSub, self).__init__(Box, null,  **kwargs_)
supermod.BoundingShapeType.subclass = BoundingShapeTypeSub
# end class BoundingShapeTypeSub


class PointPropertyTypeSub(supermod.PointPropertyType):
    def __init__(self, remoteSchema=None, type_='simple', href=None, role=None, arcrole=None, title=None, show=None, actuate=None, Point=None, **kwargs_):
        super(PointPropertyTypeSub, self).__init__(remoteSchema, type_, href, role, arcrole, title, show, actuate, Point,  **kwargs_)
supermod.PointPropertyType.subclass = PointPropertyTypeSub
# end class PointPropertyTypeSub


class PolygonPropertyTypeSub(supermod.PolygonPropertyType):
    def __init__(self, remoteSchema=None, type_='simple', href=None, role=None, arcrole=None, title=None, show=None, actuate=None, Polygon=None, **kwargs_):
        super(PolygonPropertyTypeSub, self).__init__(remoteSchema, type_, href, role, arcrole, title, show, actuate, Polygon,  **kwargs_)
supermod.PolygonPropertyType.subclass = PolygonPropertyTypeSub
# end class PolygonPropertyTypeSub


class LineStringPropertyTypeSub(supermod.LineStringPropertyType):
    def __init__(self, remoteSchema=None, type_='simple', href=None, role=None, arcrole=None, title=None, show=None, actuate=None, LineString=None, **kwargs_):
        super(LineStringPropertyTypeSub, self).__init__(remoteSchema, type_, href, role, arcrole, title, show, actuate, LineString,  **kwargs_)
supermod.LineStringPropertyType.subclass = LineStringPropertyTypeSub
# end class LineStringPropertyTypeSub


class MultiPointPropertyTypeSub(supermod.MultiPointPropertyType):
    def __init__(self, remoteSchema=None, type_='simple', href=None, role=None, arcrole=None, title=None, show=None, actuate=None, MultiPoint=None, **kwargs_):
        super(MultiPointPropertyTypeSub, self).__init__(remoteSchema, type_, href, role, arcrole, title, show, actuate, MultiPoint,  **kwargs_)
supermod.MultiPointPropertyType.subclass = MultiPointPropertyTypeSub
# end class MultiPointPropertyTypeSub


class MultiLineStringPropertyTypeSub(supermod.MultiLineStringPropertyType):
    def __init__(self, remoteSchema=None, type_='simple', href=None, role=None, arcrole=None, title=None, show=None, actuate=None, MultiLineString=None, **kwargs_):
        super(MultiLineStringPropertyTypeSub, self).__init__(remoteSchema, type_, href, role, arcrole, title, show, actuate, MultiLineString,  **kwargs_)
supermod.MultiLineStringPropertyType.subclass = MultiLineStringPropertyTypeSub
# end class MultiLineStringPropertyTypeSub


class MultiPolygonPropertyTypeSub(supermod.MultiPolygonPropertyType):
    def __init__(self, remoteSchema=None, type_='simple', href=None, role=None, arcrole=None, title=None, show=None, actuate=None, MultiPolygon=None, **kwargs_):
        super(MultiPolygonPropertyTypeSub, self).__init__(remoteSchema, type_, href, role, arcrole, title, show, actuate, MultiPolygon,  **kwargs_)
supermod.MultiPolygonPropertyType.subclass = MultiPolygonPropertyTypeSub
# end class MultiPolygonPropertyTypeSub


class MultiGeometryPropertyTypeSub(supermod.MultiGeometryPropertyType):
    def __init__(self, remoteSchema=None, type_='simple', href=None, role=None, arcrole=None, title=None, show=None, actuate=None, MultiGeometry=None, **kwargs_):
        super(MultiGeometryPropertyTypeSub, self).__init__(remoteSchema, type_, href, role, arcrole, title, show, actuate, MultiGeometry,  **kwargs_)
supermod.MultiGeometryPropertyType.subclass = MultiGeometryPropertyTypeSub
# end class MultiGeometryPropertyTypeSub


class CssParameterSub(supermod.CssParameter):
    def __init__(self, expression=None, name=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(CssParameterSub, self).__init__(expression, name, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.CssParameter.subclass = CssParameterSub
# end class CssParameterSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'StyledLayerDescriptor'
        rootClass = supermod.StyledLayerDescriptor
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:sld="http://www.opengis.net/sld"',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'StyledLayerDescriptor'
        rootClass = supermod.StyledLayerDescriptor
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'StyledLayerDescriptor'
        rootClass = supermod.StyledLayerDescriptor
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:sld="http://www.opengis.net/sld"')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'StyledLayerDescriptor'
        rootClass = supermod.StyledLayerDescriptor
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
