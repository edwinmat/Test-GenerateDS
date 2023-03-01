from sld import StyledLayerDescriptor, NamedLayer, UserStyle, FeatureTypeStyle, Rule, PolygonSymbolizer, \
    Fill, Stroke, CssParameter, FilterType, BinaryComparisonOpType

mysld = StyledLayerDescriptor()

named_layer = NamedLayer()
named_layer.set_Name("Contingent style")

user_style = UserStyle()
user_style.set_Title("Suitable")
fts = FeatureTypeStyle()
r1 = Rule()
r1.set_Title("0.0-0.2")

flt = FilterType()
ilt = BinaryComparisonOpType()
# WHAT TO DO HERE??
flt.set_comparisonOps(ilt)
r1.set_Filter(flt)

ps = PolygonSymbolizer()

f = Fill()
cssp = CssParameter()
cssp.set_name("fill")
cssp.set_valueOf_("#7bffff")
# f.add_CssParameter(CssParameter(name="fill", valueOf_="#f7fbff"))
f.add_CssParameter(cssp)
ps.set_Fill(f)

s = Stroke()
cssp = CssParameter(name="stroke", valueOf_="#000000")
# cssp.set_valueOf_("#000000")
s.add_CssParameter(cssp)
s.add_CssParameter(CssParameter(name="stroke-width", valueOf_="0.5"))
ps.set_Stroke(s)

r1.add_Symbolizer(ps)
fts.add_Rule(r1)

user_style.add_FeatureTypeStyle(fts)
named_layer.add_UserStyle(user_style)
mysld.add_NamedLayer(named_layer)

print(mysld)