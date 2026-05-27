
metadata = {
    'protocolName': 'Dinosaur',
    'author': 'Opentrons <protocols@opentrons.com>',
    'description': 'Draw a picture of a dinosaur'
}

requirements = {
    'robotType': 'Flex',
    'apiLevel': '2.19'
}

def run(protocol):
    # Load Labware
    tiprack = protocol.load_labware('opentrons_flex_96_tiprack_50ul', 'C1')
    plate = protocol.load_labware('nest_96_wellplate_200ul_flat', 'D2')
    reservoir = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', 'D1')
    
    #this is the location of the trash bin and commenting it out will cause an error
    default_trash = protocol.load_trash_bin(location = "A3")
    
    # Load Pipette
    pipette = protocol.load_instrument('flex_1channel_50', 'left',tip_racks=[tiprack])

    # Solutions
    green = reservoir['A1']
    blue = reservoir['A2']

    # Wells to dispense green
    green_wells = [well for well in plate.wells(
        'E1', 'D2', 'E2', 'D3', 'E3', 'F3', 'G3', 'H3',
        'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'C5', 'D5',
        'E5', 'F5', 'G5', 'C6', 'D6', 'E6', 'F6', 'G6',
        'C7', 'D7', 'E7', 'F7', 'G7', 'D8', 'E8', 'F8',
        'G8', 'H8', 'E9', 'F9', 'G9', 'H9', 'F10', 'G11',
        'H12')]

    # Wells to dispense blue
    blue_wells = [well for well in plate.wells(
                  'C3', 'B4', 'A5', 'B5', 'B6', 'A7', 'B7',
                  'C8', 'C9', 'D9', 'E10', 'E11', 'F11', 'G12')]

    # set clearance for well bottoms
    pipette.well_bottom_clearance.aspirate = 6
    pipette.well_bottom_clearance.dispense = 10

    # Distribute green solution to well - 50 uL to each well
    pipette.pick_up_tip()
    for well in green_wells:
        pipette.transfer(50, green, well, new_tip='never')
    
    # Drop the tip after all transfers for this stock solution
    pipette.drop_tip(default_trash)
    
    
    # Distribute blue solution to wells - 50 uL to each well
    pipette.pick_up_tip()
    for well in blue_wells:
        pipette.transfer(50, blue, well, new_tip='never')
    
    # Drop the tip after all transfers for this stock solution
    pipette.drop_tip(default_trash)


