<h1>Python - Finite Element Method (FEM)</h1>



<h2>Description</h2>
The project consists of solving the given task using a scheme employing the Finite Element Method for provided data. The solution to the task is presented in the form of a displacement plot at the finite element mesh nodes. The obtained results are compared with the analytical solution at the specified point.
<br />
<p align = "center">
 <br />
<img src="https://i.imgur.com/zd2bmRi.png" height="80%" width="80%" alt="scheme"/>
 <br /> <br />
 Beam force values ​​and other data enabling solving the task using the FEM method.
 <img src="https://i.imgur.com/AKJTs98.png" height="80%" width="80%"  alt="values"/> <br>
</p>

<h2>Languages and Utilities Used</h2>

- <b>Python</b>

<h2>Environments Used</h2>

- <b>PyCharm 2023.3.3</b>

<h2>Libraries Used</h2>

- <b>numpy</b>
- <b>matplotlib</b>

<h2>Program walk-through:</h2>

<p align="center">
Creating the stiffness matrix of a beam element <br/>
<img src="https://i.imgur.com/UwhIF1S.png" width="80%" alt ="ke"  width="80%"/>
<br />
<br />
Creating a global stiffness matrix:  <br/>
<img src="https://i.imgur.com/hCmyxCE.png" alt="Global marix " width="80%"/>
 <img src="https://i.imgur.com/0L7TFOK.png" alt="KK" width="80%"/>
<br />
<br />
Applying boundary conditions: <br/>
<img src="https://i.imgur.com/WREGb5y.png" width="80%" alt="boundaryConditions"/>
<br />
 boundary conditions for the scheme: <br/>
 <img src="https://i.imgur.com/FJPPM3E.png"  alt="conditions"/>
<br />
 <br />
Solving for displacement vector:  <br/>
<img src="https://i.imgur.com/8lU3NXp.png" width="80%" alt = "displacement vector"/>
<br />
<br />
results:  <br/>
<img src="https://i.imgur.com/t5id8vp.png" width="80%" alt="plot"/>
 <img src="https://i.imgur.com/wVPcKBl.png" width="80%" alt="error"/>


<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
