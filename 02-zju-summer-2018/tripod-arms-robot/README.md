# Tripod Arms Grabbing Robot based on Delta 3D Printer

- Advisor: Prof. Senyang Wu
- Group Members: Zhijing Hu, Keqin Wang


# MATLAB File Introduction
- This example shows how to use generalized inverse kinematics to plan a joint-space trajectory for a robotic manipulator. It combines multipleconstraints to generate a trajectory 
that guides the gripper to a cup resting on a table. These constraints ensure that the gripper approaches the cup in a straight line and that the gripper remains at a safe
distance from the table, without requiring the poses of the gripper to be determined in advance.
 
- Copyright 2016 The MathWorks, Inc.

- This example uses a model of the KUKA LBR iiwa, a 7 degree-of-freedom robot manipulator. |<docid:robotics_ref.bvlvwcs-1 importrobot>| 
generates a |<docid:robotics_ref.bvan8uq-1 robotics.RigidBodyTree>| model from a description stored in a Unified Robot Description Format (URDF) file.
