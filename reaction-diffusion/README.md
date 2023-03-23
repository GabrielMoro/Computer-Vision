# Reaction Diffusion

A reaction-diffusion system is defined by a system of partial differential equations (PDEs) used for chemical and biological simulations. Such a system describes the interactions between two reagents in space and time, where one reagent works as an activator, accelerating the reagent production, and the other as an inhibitor that slows it down.

The implemented model ([Malheiros, Fensterseifer and Walter (2020)](https://mgmalheiros.github.io/research/leopard/)) is described by the equations

$$
\begin{align}
\\
\frac{\partial{a}}{\partial{t}} &= 16 - a b + r s \nabla^2 a
\\
\frac{\partial{b}}{\partial{t}} &= a b - b - 12 + s \nabla^2 b
\end{align}
$$

where $a, b$ are the reagents concentrations, $r$ is the diffusion 'ratio', $s$ the diffusion 'scale', and $\nabla_2$ (Laplacian) is the concentration of a reagent at a location with respect to nearby .concentration.

## Result examples (Using Euler method)

### Isotropic diffusion

![Isotropic diffusion](https://user-images.githubusercontent.com/22036337/227230384-d212db5f-1386-4007-b2a6-5cdc7364c830.png)

![Isotropic gif](https://user-images.githubusercontent.com/22036337/227232692-06533ae9-9110-4db7-8792-0dc4ffc71462.gif)

### Anisotropic diffusion

![Anisotropic diffusion](https://user-images.githubusercontent.com/22036337/227230504-c4ffd1c9-d8ef-4584-bc8e-ebfd0b0d7735.png)

![Anisotropic gif](https://user-images.githubusercontent.com/22036337/227232893-826cef49-476c-47cd-8d1c-ea6b7659da04.gif)

### Non convergent diffusion

![non_convergence](https://user-images.githubusercontent.com/22036337/227233103-69ec2308-963f-4f81-b917-59a8f1551d32.gif)
