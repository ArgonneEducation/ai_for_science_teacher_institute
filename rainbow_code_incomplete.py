from opentrons import protocol_api

# Metadata
metadata = {
    'protocolName': '????Name your protocol-maybe your names????',
    'author': 'Coding_For_Science_Team',
    'description': 'Mixing colored solutions to create rainbow colors'
}

# Requirements Library defining the robot type and API level
requirements = {
    "robotType": "Flex",
    "apiLevel": "2.19"
}

def run(protocol: protocol_api.ProtocolContext):

    #Labware deck setup - set the tiprack in slot C1, the wellplate for the rainbow column in slot D2, and the stock solutions in slot D1
    tip_rack = protocol.load_labware(
        load_name='opentrons_flex_96_tiprack_50ul',
        location='c1'
    )
    plate = protocol.load_labware(
        load_name='nest_96_wellplate_200ul_flat',
        location='d2'
    )
    well_reservoir = protocol.load_labware(
        load_name='opentrons_6_tuberack_nest_50ml_conical',
        location='d1'
    )
    #this is the location of the trash bin
    default_trash = protocol.load_trash_bin(location = "A3") 
    # While default_trash is not called, deleting this leads to an error.

    # Pipette loading - identify the pipette type and location
    pipette = protocol.load_instrument(
        'flex_1channel_50', 'left', tip_racks=[tip_rack])

    # Define stock solutions - locations of the stock solutions in the reservoir
    stock_locations = {
        'red': well_reservoir.wells_by_name()['A1'], # top left well in the reservoir
        'yellow': well_reservoir.wells_by_name()['A2'], # top middle well in the reservoir
        'blue': well_reservoir.wells_by_name()['A3'] # top right well in the reservoir
    }

    # Define locations for rainbow colors wells

    # The well plate is a 96 well plate, laid out as shown below:
    """  3 double quotation marks allow for multi-line comments

       1    2    3    4    5    6    7    8    9    10   11   12
    A     |    |    |    |    |    |    |    |    |    |    |    |
       -----------------------------------------------------------
    B     |    |    |    |    |    |    |    |    |    |    |    |
       -----------------------------------------------------------
    C     |    |    |    |    |    |    |    |    |    |    |    |
       -----------------------------------------------------------
    D     |    |    |    |    |    |    |    |    |    |    |    |
       -----------------------------------------------------------
    E     |    |    |    |    |    |    |    |    |    |    |    |
       -----------------------------------------------------------
    F     |    |    |    |    |    |    |    |    |    |    |    |
       -----------------------------------------------------------
    G     |    |    |    |    |    |    |    |    |    |    |    |
       -----------------------------------------------------------
    H     |    |    |    |    |    |    |    |    |    |    |    |
    """

 # Check with your instructor to see what column you should be using and adjust the value in the column variable.
    column = ?

# Define the destinations for the rainbow colors in the well plate
    color_locations = {
        'red': plate.wells_by_name()[f'A{column}'],
        'orange': plate.wells_by_name()[f'B{column}'],
        'yellow': plate.wells_by_name()[f'C{column}'],  
        'green': plate.wells_by_name()[f'D{column}'],
        'blue': plate.wells_by_name()[f'E{column}'],
        'violet': plate.wells_by_name()[f'F{column}']
    }
# define tip rack locations
    tip_locations = {
        'red': tip_rack.wells_by_name()[f'A{column}'],
        'yellow': tip_rack.wells_by_name()[f'B{column}'],
        'blue': tip_rack.wells_by_name()[f'C{column}']
    }
    # Color Compositions - not used - just for reference
    color_compositions = {
        'red': {'red': 50},
        'orange': {'red': 25, 
                   'yellow': 25
                   },
        'yellow': {'yellow': 50},
        'green': {'yellow': 25, 
                  'blue': 25
                  },
        'blue': {'blue': 50},
        'violet': {'blue': 25, 
                   'red': 25
                   }
    }
    # set clearance for well bottoms - the number is how many mm above the bottom of the well the pipette will be
    pipette.well_bottom_clearance.aspirate = 75 # pipette tip is 57.90 mm long, the tubes are 120 mm tall,
    # so this will keep the tip from going too far down into the tube

    pipette.well_bottom_clearance.dispense = 10 # this will allow the pipette to dispense without contacting the liquid in the tube.
    
    # function for mixing colors
    def mix_colors(tip_locations: dict[str, protocol_api.Labware], stock_locations: dict[str, protocol_api.Well],color_locations: dict[str, protocol_api.Well]):
        
        pipette.pick_up_tip(tip_locations['red'])
        # transfer red solution to destination wells

	    #complete the code
        pipette.aspirate(50, stock_locations['red']) # draw in 50 uL from the 'red' stock
        pipette.dispense(50, color_locations['red']) # dispense 50 uL into the 'red' well of the rainbow
        pipette.touch_tip(speed=20, radius=0.85) # please leave these values alone - this command moves the tip to the sides of the well to release drops.

	    # prepare orange and violet wells with red liquid        
        pipette.aspirate(?????, ?????) # draw in 25 uL from the 'red' stock
	    pipette.dispense(?????, ?????) # 25 uL dispensed in the "orange" well of the rainbow
	    pipette.touch_tip(speed=20, radius=0.85) # please leave these values alone - this command moves the tip to the sides of the well to release drops.
                   
	    pipette.aspirate(?????, ?????) # draw in 25 uL from the 'red' stock
	    pipette.dispense(?????, ?????) # 25 uL dispensed in the "violet" well of the rainbow
	    pipette.touch_tip(speed=20, radius=0.85) # please leave these values alone
                         
        pipette.drop_tip(default_trash)
    

        #complete the code for the yellow solution distribution
        pipette.pick_up_tip(tip_locations[?])
        # transfer yellow solution to destination wells
        pipette.aspirate(?????, ?????)
	    pipette. dispense(?????, ?????) 
	    pipette.touch_tip(speed=20, radius=0.85) # please leave these values alone - this command moves the tip to the sides of the well to release drops.

	    pipette.aspirate(?????, ?????)
	    pipette. dispense(?????, ?????)
	    pipette.touch_tip(speed=20, radius=0.85) # please leave these values alone
                   
	    pipette.aspirate(?????, ?????)
	    pipette. dispense(?????, ?????)
	    pipette.touch_tip(speed=20, radius=0.85) # please leave these values alone
                         
        pipette.drop_tip(default_trash)


        # complete the code for the blue solution distribution
        pipette.pick_up_tip(tip_locations[?])
        # transfer blue solution to destination wells
	    pipette.aspirate(???, ?????)
	    pipette. dispense(???, ????)
	    pipette.touch_tip(speed=20, radius=0.85) # please leave these values alone - this command moves the tip to the sides of the well to release drops.
        
	    pipette.aspirate(???, ?????)
	    pipette.dispense(?,????)
	    pipette.touch_tip(speed=20, radius=0.85) # please leave these values alone
           
	    pipette.aspirate(???, ?????)
	    pipette.dispense(?,????)
	    pipette.touch_tip(speed=20, radius=0.85) # please leave these values alone
                         
        pipette.drop_tip(default_trash)


    # Perform mixing for all colors
    mix_colors(tip_locations, stock_locations, color_locations)
