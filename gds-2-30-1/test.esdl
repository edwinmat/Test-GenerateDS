<?xml version="1.0" encoding="UTF-8"?>
<esdl:EnergySystem xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:esdl="http://www.tno.nl/esdl"
xsi:schemaLocation="http://www.tno.nl/esdl ../esdl/model/esdl.ecore" name="My EnergySystem">
    <esdl:instance name="First instance">
        <esdl:area name="City">
            <esdl:Asset name="WindTurbine" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="WindTurbine" power="3.000000e+06">
                <esdl:Port id="30055b3e-8565-4dc4-87c1-e362e5014f7c" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="OutPort" connectedTo="6f46540f-6e5f-49e3-b033-ffc1eef74aea"/>
            </esdl:Asset>
            <esdl:Asset name="Aggregated households" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="AggregatedBuilding">
                <esdl:Asset name="ElectricityDemand" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ElectricityDemand">
                    <esdl:Port id="cc2f55c1-a944-4df3-9ebb-9081ab354b9b" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="InPort" connectedTo="e1a197d2-e513-4d44-9eee-fd84fe862d0f"/>
                </esdl:Asset>
            </esdl:Asset>
            <esdl:Asset name="Electricity Network" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ElectricityNetwork">
                <esdl:Port id="6f46540f-6e5f-49e3-b033-ffc1eef74aea" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="InPort" connectedTo="30055b3e-8565-4dc4-87c1-e362e5014f7c"/>
                <esdl:Port id="e1a197d2-e513-4d44-9eee-fd84fe862d0f" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="OutPort" connectedTo="cc2f55c1-a944-4df3-9ebb-9081ab354b9b"/>
</esdl:Asset>
        </esdl:area>
    </esdl:instance>
</esdl:EnergySystem>
