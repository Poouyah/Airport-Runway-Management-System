# 🛫 Airport Runway Management System

### 📜 Overview

This Python program simulates an airport runway management system. The airport has k runways, each numbered from 1 to k. Airplanes, each identified by a unique 10-digit `<ID>`, can be in one of four possible states at any given time:

At the airport, not occupying a runway.

At the airport, occupying a runway and taking off.

At the airport, occupying a runway and landing.

Not at the airport.

The system processes various commands to manage the take-off, landing, and status of airplanes and runways.

### 🛠️ Features

Manage Airplanes: Track the status of airplanes, including whether they are at the airport, taking off, or landing.

Runway Assignment: Automatically assign the first available runway for take-off or landing.

Command Processing: Handle multiple commands to manage and query the status of airplanes and runways.


### 📥 Input

Initial Setup:

Two integers n (number of airplanes at the airport) and k (number of runways).
n lines each containing a unique 10-digit airplane ID.
An integer q representing the number of commands to be processed.

Commands:

- `TAKE-OFF <ID>`: Manage the take-off request of the airplane with the specified ID.

* `LANDING <ID>`: Manage the landing request of the airplane with the specified ID.

+ `PLANE-STATUS <ID>`: Query the current status of the airplane with the specified ID.

- `BAND-STATUS <LINE>`: Query the status of the specified runway.


### 📤 Output

The program produces output based on the commands:

- `TAKE-OFF`: Outputs the status of the take-off request.

* `LANDING`: Outputs the status of the landing request.

+ `PLANE-STATUS`: Outputs the current status of the specified airplane.

- `BAND-STATUS`: Outputs the current status of the specified runway.

### 📚 Example

Input:

```
2 5
1000000000
0002000000
10
TAKE-OFF 0002000000
LANDING 1234567891
PLANE-STATUS 1234567891
BAND-STATUS 5
LANDING 9876543219
LANDING 5555555555
BAND-STATUS 2
TAKE-OFF 1000000000
LANDING 3434343434
PLANE-STATUS 6666666666
```
Output:

```
3
1234567891
FREE
NO FREE BOUND
4
```
