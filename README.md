# Extension of the Sines method (Sines++)

<p>In materials science, fatigue is the weakening of a material caused by cyclic loading that results in progressive and localized structural damage and the growth of cracks. Once a fatigue crack has initiated, each loading cycle will grow the crack a small amount, typically producing striations on some parts of the fracture surface. The crack will continue to grow until it reaches a critical size, which occurs when the stress intensity factor of the crack exceeds the fracture toughness of the material, producing rapid propagation and typically complete fracture of the structure.</p>

<p>Multiaxial fatigue is a general term that may be used to describe loading and/or loading plus geometry conditions resulting in complex states of stresses and strains, either locally or globally. More specifically, multiaxial loading will result in a state of stress and/or strain, which manifests as two or more components in the stress or strain tensor. An example of a stress tensor resulting at the surface of a component experiencing externally applied normal force, coupled with an externally applied toque.</p>

<p>Multiaxial loads are common for many components and structures. Even under uniaxial loads multiaxial stresses often exist, for example due to geometric constraints at notches. Such multiaxial loads and stress states are frequently encountered in many industries, including automotive, aerospace, and power generation, among others. In order to describe the multiaxial high cycle fatigue behavior of materials, one was proposed the modified Sines method (Sines++) [1].</p>
<p align="center">
  <img src="https://github.com/yanicen1/multiaxial-fatigue-modified-model-Sines-/blob/master/Fig.1.png" width="700" title="hover text">
</p>
<p>where <i>I<sub>2a</sub></i> and <i>I<sub>2m</sub></i> are the amplitude and the mean value of the second invariant of the stress deviator tensor, <i>I<sub>1m</sub></i> and <i>I<sub>1a</sub></i> are the amplitude and the mean value of the first invariant of the stress tensor.</p>
<p>The the model parameters A, B, С and D were determined as follows:</p>
<p align="center">
  <img src="https://github.com/yanicen1/multiaxial-fatigue-modified-model-Sines-/blob/master/Fig.2.png" width="860" title="hover text">
</p>
<p>where <i>N<sub>σ</sub></i> and <i>N<sub>τ</sub></i> are values of the predicted fatigue life (normal and shear axis), <i>σ<sub>u</sub></i> is the ultimate tensile strength, <i>τ<sub>u</sub></i> is the shear strength, <i>τ'<sub>f</sub></i> is the shear fatigue strength coefficient, <i>b<sub>0</sub></i> is the shear fatigue strength exponent, <i>σ'<sub>f</sub></i> is the fatigue strength coefficient, <i>b</i> is the fatigue strength exponent, <i>υ<sub>σ</sub></i> and <i>υ<sub>τ</sub></i> are load frequencies for normal and shear axis.</p>
<p>The purpose is to find <i>N</i>, <i>N<sub>σ</sub></i> and <i>N<sub>τ</sub></i> for the model Sines++.</p>

<h4>Input:</h4>
<p>1. Store values of mechanical properties of used material in the file 'mechanical_properties.csv'.</p>
<p>2. Store parameters of fatigue paths in the file 'fatigue_tests.csv'.</p>
<p>3. Run the program.</p>
<h4>Output:</h4>
<p>4. Number and percentage of values of predicted fatigue life that are out of the ±2 and 3-factor error range.</p>
<p>5. Standard error:</p>
<p>
  <img src="https://github.com/yanicen1/multiaxial-fatigue-modified-model-Sines-/blob/master/Fig.3.png" width="190" title="hover text">
</p>
<p>where <i>N</i> and <i>N<sub>ex</sub></i> are predicted and experimental fatigue life, <i>n</i> is a number of tests.</p>
<p>6. Comparison of model prediction with experimental results (Fig. 1).</p>
<p align = 'center'>
  <img src="https://github.com/yanicen1/multiaxial-fatigue-modified-model-Sines-/blob/master/Fig.0.png" width="500" title="hover text">
</p>
<p align = 'center'>Figure 1. Comparison of model prediction with experimental results.</p>

<p>[1] A.S. Iankin et alii. Influence of static mean stresses on the fatigue behavior of 2024 aluminum alloy under multiaxial loading // Frattura ed Integrità Strutturale, 51 (2020) 151-163; https://doi.org/10.3221/IGF-ESIS.51.12</p>
<br>
<p>If you have questions, please feel free to contact me: 
Andrei Iankin, yas.cem.yanicen@gmail.com</p>
