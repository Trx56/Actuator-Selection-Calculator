def actuator_selector():
    print("--- Robotic Actuator Selection Calculator ---")
    
    # Gather physical requirements
    try:
        payload = float(input("Enter required payload or force (in kg): "))
        speed = float(input("Enter required speed (1 = Slow/Precise, 2 = High Speed): "))
        battery_powered = input("Is the robot battery-powered/mobile? (y/n): ").strip().lower()
    except ValueError:
        print("Invalid input. Please enter numbers for payload and speed.")
        return

    print("\n--- Recommendation ---")
    
    # Selection logic based on your flowchart
    if payload > 500:
        print("Selection: Hydraulic Actuator (e.g., Bosch Rexroth CDH1)")
        print("Reason: Heavy load detected. Hydraulics provide maximum force density.")
    elif speed == 2 and battery_powered == 'n':
        print("Selection: Pneumatic Actuator (e.g., Festo ADN)")
        print("Reason: Fast, clean motion required without strict battery limits.")
    elif battery_powered == 'y':
        if speed == 2:
            print("Selection: Brushless DC (BLDC) (e.g., ODrive D6374)")
            print("Reason: High speed and power efficiency needed for mobile battery operation.")
        else:
            print("Selection: DC Servo (e.g., TowerPro MG996R) or Brushed DC")
            print("Reason: Precise holding torque and simple control for low-speed battery applications.")
    else:
        print("Selection: Geared Brushed DC Motor (e.g., Maxon DCX 12V)")
        print("Reason: Balanced industrial application requiring reliable continuous torque.")

# Run the calculator
actuator_selector()
