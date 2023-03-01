generateDS.py -m -f -o sld.py -s sldsubs.py StyledLayerDescriptor.xsd
@REM generateDS.py -f --no-namespace-defs -o sld.py -s sldsubs.py StyledLayerDescriptor.xsd
@REM generateDS.py --namespacedef='xsi:schemaLocation="http://www.opengis.net/sld" xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"' -o sld.py -s sldsubs.py StyledLayerDescriptor.xsd
