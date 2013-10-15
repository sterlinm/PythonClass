"""
Inventory
---------

Calculate and report the current inventory in a warehouse.

Assume the warehouse is initially empty.

The string, warehouse_log, is a stream of deliveries to 
and shipments from a warehouse.  Each line represents
a single transaction for a part with the number of
parts delivered or shipped.  It has the form::

    part_id count

If "count" is positive, then it is a delivery to the
warehouse. If it is negative, it is a shipment from
the warehouse.

See :ref:`inventory-solution`.
"""

from collections import defaultdict

warehouse_log = """ frombicator      10
                    whitzlegidget    5
                    splatzleblock    12
                    frombicator      -3
                    frombicator      20
                    foozalator       40
                    whitzlegidget    -4
                    splatzleblock    -8
                """                            

warehouse_list = warehouse_log.strip().splitlines()
current_inventory = defaultdict(lambda: 0)

for order in warehouse_list:
    part_id, count = order.strip().split()
    current_inventory[part_id] += int(count)

for part in current_inventory:
    print '{part:20}{num}'.format(part=part,num=current_inventory[part])