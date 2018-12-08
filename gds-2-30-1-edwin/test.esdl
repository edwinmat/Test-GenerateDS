<?xml version="1.0" encoding="UTF-8"?>
<esdl:EnergySystem xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:esdl="http://www.tno.nl/esdl"
xsi:schemaLocation="http://www.tno.nl/esdl ../esdl/model/esdl.ecore" name="My EnergySystem">
    <instance name="First instance">
        <area name="City">
            <asset name="WindTurbine" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:WindTurbine" power="3000000.000000">
                <port id="c7e370cb-bdf2-41aa-92a0-bf9f0912248d" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:OutPort" connectedTo="519d5c5e-a40e-4472-b8d8-27350c1adee7"/>
            </asset>
            <asset name="Aggregated households" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:AggregatedBuilding">
                <asset name="ElectricityDemand" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:ElectricityDemand">
                    <port id="08930d1b-23d0-47c9-bac3-3a9ce8968c8d" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:InPort" connectedTo="2ff738de-e8ad-4714-b47c-048526130118"/>
                </asset>
            </asset>
            <asset name="Electricity Network" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:ElectricityNetwork">
                <port id="519d5c5e-a40e-4472-b8d8-27350c1adee7" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:InPort" connectedTo="c7e370cb-bdf2-41aa-92a0-bf9f0912248d"/>
                <port id="2ff738de-e8ad-4714-b47c-048526130118" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:OutPort" connectedTo="08930d1b-23d0-47c9-bac3-3a9ce8968c8d"/>
</asset>
        </area>
    </instance>
</esdl:EnergySystem>
