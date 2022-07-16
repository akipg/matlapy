# matlapy

**in development**

## environments
Python >= 3.6

## installation

1. Install matlapy
```

```

2. Attach Python to MATLAB

    Refer to [**MathWorks' guide**](https://jp.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html) to attach python to matlab.

    And also refer to [*MATLAB vs Python versions*](https://www.mathworks.com/content/dam/mathworks/mathworks-dot-com/support/sysreq/files/python-compatibility.pdf)


## How will matlapy work?

```python
import matlapy import Matlapy

# Start MATLAB
mpy = Matlapy()
mpy.start_matlab()

# Create a new model
mdl = mpy.new_system("sample_model")

# Add block (1)
constant1 = mpy.blocks.Constant(name="Constant1", value=10)
mdl.addBlock(constant1)
# Add block (2)
constant2 = mdl.addBlock("simulink/Sources/Constant")

# Arrange block's position
constant1.moveTo(10, 20) # The Constant block moves to (x,y)=(10,20)
constant1.moveX(10) # The Constant block moves 10 points along x

# Align block position by another block
constant2.alignTo(constant1, align=2, anchor=0, marginX=20)
# => Constant2 moves to right of Constant1 with x margin 20

# Connect to block
constant = mdl.addBlock("simulink/Sources/Constant") 
outport = mdl.addBlock("simulink/Sinks/Outport")
constant.connectTo(outport, dstport=1, srcport=1) # Add line

# Daisy chain
mdl.addBlock("simulink/Sources/Constant").moveTo(0,0).connectTo(anotherblock)

# Create subsystem
subsystem1 = mdl.addSubsystem("layer1")
print(subsystem1.path) # => "sample_model/layer1"
# Add block to subsystem
constant = subsystem1.addBlock("simulink/Sources/Constant")
# Rename block name
constant.name = "ConstA"
# Get the block informations
print(constant.path) # => "sample_model/layer1/ConstA"
print(constant.parent) # => "sample_model/layer1"

# Find import blocks
print(mdl.find_systems("SearchDepth", 1, "BlockType", "Inport"))

# Save system
mdl.save()


```

## alpha version
```
```