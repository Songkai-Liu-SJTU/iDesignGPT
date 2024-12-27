# iDesignGPT: large language model agentic workflows boost engineering design

> **Paper under submission**: The related paper is currently under submission. Reviewers can refer to this GitHub page for further details.

![fig2-3](https://github.com/user-attachments/assets/61c84c04-be06-475a-bb98-5b75139f10a0)

iDesignGPT is a novel framework that integrates large language model with established design methodologies to enable dynamic multi-agent collaboration for problem refinement, information gathering, design space exploration, and iterative optimization.

## Project Structure

This repository consists of two main parts: `Data` and `Code`.

### Data
This section includes the experimental data and results used in the study. The dataset consists of experimental data from various design scenarios and the optimized results generated by the iDesignGPT framework.

- The `data/` folder contains the relevant experimental data and results.
- Please refer to the corresponding README files in the `data/` folder for details on data formats and usage.

### Code
This section showcases how to build and run the agents' prompts within the iDesignGPT framework, constructed on the [FastGPT](https://github.com/labring/FastGPT?tab=readme-ov-file) platform. This repository primarily focuses on the *prompts* used by the agents, rather than traditional source code.

- The core functionality is not traditional “code,” but rather agent *prompts* used for design optimization.
- You will need to use the FastGPT platform to run these prompt scripts for design exploration and optimization.

#### Using FastGPT
iDesignGPT is built on the [FastGPT](https://github.com/labring/FastGPT?tab=readme-ov-file) platform. You need to follow the FastGPT setup instructions to run and test these prompts.

- Clone the [FastGPT repository](https://github.com/labring/FastGPT?tab=readme-ov-file) and follow the setup instructions in its README file.
- Then, load and run the prompt scripts from this repository within the FastGPT platform to begin experimentation.

### How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/iDesignGPT.git
   cd iDesignGPT
   ```
   
2. Install and set up FastGPT: Please refer to the FastGPT README for installation instructions.

3. Run the iDesignGPT design agents (prompts): Load the relevant prompt files into the FastGPT platform and execute them.
   
## Results and Visualization
This project includes several design optimization results from the experiments. You can find the specific data in the data/ folder.

   ```bash
   /data
       ├── experiment1_results.csv
       ├── experiment2_results.csv
       └── ...
   ```

## Contributing

Contributions to this project are welcome, especially in the following areas:

- Testing and validating the functionality of iDesignGPT.
- Contributing new design tasks and optimization algorithms.
- Providing improvements and feedback on the existing model.

If you're interested in contributing, please open an Issue to discuss your contributions, then submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
If you'd like to experience iDesignGPT, feel free to contact me at [lsk555763@sjtu.edu.cn] with your interest. I can share a version of the iDesignGPT that I have personally built and set up for further testing and exploration.
