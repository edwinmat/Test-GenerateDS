import esdl_sup as esdl
import uuid

xml_namespace = ('xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\nxmlns:esdl="http://www.tno.nl/esdl"\nxsi:schemaLocation="http://www.tno.nl/esdl ../esdl/model/esdl.ecore"')

def write_energysystem_to_file(filename, es):
    f = open(filename, 'w+', encoding='UTF-8')
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    es.export(f, 0, namespaceprefix_='', name_='esdl:EnergySystem', namespacedef_=xml_namespace, pretty_print=True)
    f.close()

if __name__ == "__main__":

    energy_system = esdl.EnergySystem()
    energy_system.set_name('My EnergySystem')

    instance = esdl.Instance()
    instance.set_name('First instance')
    energy_system.add_instance(instance)

    area = esdl.Area()
    area.set_name('City')
    instance.set_area(area)

    wind_turbine = esdl.WindTurbine()
    wind_turbine.set_name('WindTurbine')
    wind_turbine.set_power(3000000)
    wt_port = esdl.OutPort()
    wt_port.set_id(uuid.uuid4())
    wind_turbine.add_port_with_type(wt_port)
    area.add_asset_with_type(wind_turbine)

    electr_demand = esdl.ElectricityDemand()
    electr_demand.set_name('ElectricityDemand')
    ed_port = esdl.InPort()
    ed_port.set_id(uuid.uuid4())
    electr_demand.add_port_with_type(ed_port)

    aggr_building = esdl.AggregatedBuilding()
    aggr_building.set_name('Aggregated households')
    aggr_building.add_asset_with_type(electr_demand)
    area.add_asset_with_type(aggr_building)

    elec_network = esdl.ElectricityNetwork()
    elec_network.set_name('Electricity Network')
    en_wt_port = esdl.InPort()
    en_wt_port.set_id(uuid.uuid4())
    elec_network.add_port_with_type(en_wt_port)
    en_ed_port = esdl.OutPort()
    en_ed_port.set_id(uuid.uuid4())
    elec_network.add_port_with_type(en_ed_port)
    area.add_asset_with_type(elec_network)

    en_wt_port.set_connectedTo(wt_port.get_id())
    en_ed_port.set_connectedTo(ed_port.get_id())
    wt_port.set_connectedTo(en_wt_port.get_id())
    ed_port.set_connectedTo(en_ed_port.get_id())

    write_energysystem_to_file('test.esdl', energy_system)
