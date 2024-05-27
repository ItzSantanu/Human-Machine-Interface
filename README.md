# Human-Machine Interface (HMI) for 6-RSS Parallel Manipulator

## Overview

This repository contains the Human-Machine Interface (HMI) developed for the 6-RSS parallel robot manipulator as part of my summer internship project at the Robotics and Automation Lab, IIT (ISM) Dhanbad. The HMI is designed to facilitate intuitive control and monitoring of the robot's movements and functionalities.

## Features

- **Platform Translation:** Control the platform movement along the X, Y, and Z axes.
- **Platform Rotation:** Adjust the orientation of the platform around its axis.
- **Connection Management:** Scan for, connect to, and manage connections with the robot.
- **Power Control:** Manage the power status of the system, including turning on/off and halting operations.
- **Position Navigation:** Navigate the platform to specific pre-defined positions.

## Technology Stack

- **Programming Language:** Python
- **GUI Toolkit:** Toga (part of the Beeware package)
- **Compatibility:** Cross-platform support for Android, Windows, and iOS

## Installation

### Prerequisites

- Python 3.6 or higher
- Toga (part of the Beeware package)

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/ItzSantanu/Human-Machine-Interface.git
    cd Human-Machine-Interface
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the HMI application:
    ```bash
    python hmi.py
    ```

## Usage

### Main Interface

The main interface provides controls for:
- Translating the platform along the X, Y, and Z axes.
- Rotating the platform around its axis.
- Managing connections with the robot.
- Controlling the power status of the system.
- Navigating the platform to predefined positions like Home.

### Connection Management

To establish a connection with the robot:
1. Open the Connection Management section.
2. Scan for available connections.
3. Select the desired device and connect.
4. To disconnect, select the connected device and choose the disconnect option.

### Power Control

Use the Power Control section to:
- Turn the platform on or off.
- Halt any ongoing operations instantly.

### Position Navigation

Navigate the platform to predefined positions:
1. Open the Position Navigation section.
2. Select the desired position from the dropdown menu.
3. The platform will automatically move to the chosen location.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the GNU LESSER GENERAL PUBLIC LICENSE Version 2.1 License. See the [LICENSE](https://github.com/ItzSantanu/Human-Machine-Interface/blob/main/LICENSE) file for details.

## Acknowledgements

This project was developed as part of my summer internship at the Robotics and Automation Lab, IIT (ISM) Dhanbad. Special thanks to my internship supervisor, [Dr. Arun Dayal Udai](https://www.linkedin.com/in/arunudai/), and my mentors, [Mr. Himanshu Varshney](https://www.linkedin.com/in/himanshu-varshney/) and [Prof. Arka Banerjee](https://www.linkedin.com/in/arka-banerjee-29511840/), for their guidance and support.

## Contact

For any questions or inquiries, please contact me at [santanubasuray@gmail.com.com](mailto:santanubasuray@gmail.com.com).

---

By providing this detailed overview, the README file ensures that users can easily understand the purpose, setup, and usage of the HMI for the 6-RSS parallel manipulator. This makes the repository accessible and user-friendly for both developers and end-users.
