# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.12

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = C:\Users\Danj\AppData\Local\JetBrains\Toolbox\apps\CLion\ch-0\182.4323.58\bin\cmake\win\bin\cmake.exe

# The command to remove a file.
RM = C:\Users\Danj\AppData\Local\JetBrains\Toolbox\apps\CLion\ch-0\182.4323.58\bin\cmake\win\bin\cmake.exe -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Users\Danj\Desktop\Yandex_contest_mod3-4\graph_1\kruskal

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Users\Danj\Desktop\Yandex_contest_mod3-4\graph_1\kruskal\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/kruskal.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/kruskal.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/kruskal.dir/flags.make

CMakeFiles/kruskal.dir/main.cpp.obj: CMakeFiles/kruskal.dir/flags.make
CMakeFiles/kruskal.dir/main.cpp.obj: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\Danj\Desktop\Yandex_contest_mod3-4\graph_1\kruskal\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/kruskal.dir/main.cpp.obj"
	C:\MinGW\bin\g++.exe  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\kruskal.dir\main.cpp.obj -c C:\Users\Danj\Desktop\Yandex_contest_mod3-4\graph_1\kruskal\main.cpp

CMakeFiles/kruskal.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/kruskal.dir/main.cpp.i"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:\Users\Danj\Desktop\Yandex_contest_mod3-4\graph_1\kruskal\main.cpp > CMakeFiles\kruskal.dir\main.cpp.i

CMakeFiles/kruskal.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/kruskal.dir/main.cpp.s"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:\Users\Danj\Desktop\Yandex_contest_mod3-4\graph_1\kruskal\main.cpp -o CMakeFiles\kruskal.dir\main.cpp.s

# Object files for target kruskal
kruskal_OBJECTS = \
"CMakeFiles/kruskal.dir/main.cpp.obj"

# External object files for target kruskal
kruskal_EXTERNAL_OBJECTS =

kruskal.exe: CMakeFiles/kruskal.dir/main.cpp.obj
kruskal.exe: CMakeFiles/kruskal.dir/build.make
kruskal.exe: CMakeFiles/kruskal.dir/linklibs.rsp
kruskal.exe: CMakeFiles/kruskal.dir/objects1.rsp
kruskal.exe: CMakeFiles/kruskal.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Users\Danj\Desktop\Yandex_contest_mod3-4\graph_1\kruskal\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable kruskal.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\kruskal.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/kruskal.dir/build: kruskal.exe

.PHONY : CMakeFiles/kruskal.dir/build

CMakeFiles/kruskal.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\kruskal.dir\cmake_clean.cmake
.PHONY : CMakeFiles/kruskal.dir/clean

CMakeFiles/kruskal.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Users\Danj\Desktop\Yandex_contest_mod3-4\graph_1\kruskal C:\Users\Danj\Desktop\Yandex_contest_mod3-4\graph_1\kruskal C:\Users\Danj\Desktop\Yandex_contest_mod3-4\graph_1\kruskal\cmake-build-debug C:\Users\Danj\Desktop\Yandex_contest_mod3-4\graph_1\kruskal\cmake-build-debug C:\Users\Danj\Desktop\Yandex_contest_mod3-4\graph_1\kruskal\cmake-build-debug\CMakeFiles\kruskal.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/kruskal.dir/depend
