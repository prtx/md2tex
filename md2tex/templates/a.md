# Objective
The objective of the lab is to learn to design a CMOS inverter. Following are the steps associated with the objective.
- Design a schematic view of an inverter using transistors. The switching threshold should be half of VDD.
- Implement transient and DC simulation to verify inverter is symmetric
- Build layout of the inverter and implement DRC and LVS (against schematic) checks.


# Introduction
A CMOS inverter is designed using an NMOS and PMOS as shown in Figure \ref{fig:transistor_diagram_inverter}.

An inverter is symmetric if it has the same rise and fall time. Rise time is the time required for output to rise from 10\% to 90\% of VDD whereas fall time is the time required for output to from from 90\% to 10\%. In such cases input and output voltages coincide at Vdd/2. Propagation delay is the time delay between the applying of input and generation of output and is calculated as the time difference between 50\% of input rise to 50\% of output rise.

# Schematic Design

## CMOS Inverter
An inverter was designed using a standard PMOS and NMOS with both of initial width 150nm and length 50nm.

The inverter was connected to a capacitance of 5fF and a pulse voltage (1.2V, 10ps rise time, 10ps fall time, pulse width 50ns) for transient simulation(figure \ref{fig:transient_simulation}) and DC simulation(figure \ref{fig:dc_simulation}).

In figure \ref{fig:dc_simulation}, we can see that the inverter was not symmetric since the switching threshold was aprrox. $5.5V$ instead of the expected $1.2V/2=0.6V$.

## Parametric Analysis
Width of the PMOS can be adjusted in order to bring the switching threshold of the inverter to 0.6V and make the inverter symmetric. In order to do so, DC simulation of PMOS with different width ranging from 90nm to 300nm was visualized.

In figure \ref{fig:parametric_analysis}, we could see an inverter using a PMOS with width 245nm was symmetric. Thus, the width of PMOS of the original inverter was set to 245nm. Now, the rise time and fall time of the inverter should be approximately the same.

## CMOS Inverter

Rise and fall time are calculated from figure.

Propagation delay = 0.017ns

# Layout Design

After designing the schematic the same inverter sizing was used to design a layout. The length of the transistors were 300nm whereas the width of NMOS was 150nm whereas same of PMOS was 245nm.

# Verification
After designing the layout, following verifications were done.

## Design Rule Checking (DRC)
DRC checks the layout for possible rule violations such as invalid sizing of components or not enough space between them. Corrections suggested by DRC were implemented until no errors were remaining.

## Layout versus Schematic Checking (LVS)
LVS compared the layout designed against the schematic. It showed the layout mimicked the functionality of the schematic of the inverter and thus was properly designed.

# Conclusion
Thus, a CMOS schematic was designed in this lab. The inverter was not found to be symmetric so PMOS width over a range were simulated to find the PMOS with that would make the inverter symmetric. Rise time, fall time and propagation delay were measured and finally, a **subsequent *layout* was** designed and **verified** ***against*** the *inverter*.
