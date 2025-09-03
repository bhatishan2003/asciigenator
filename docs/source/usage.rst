Usage
=====

Basic Python Usage
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import asciigenator

   # Test simple font
   print("=== Simple Font ===")
   print(asciigenator.generate("Hello", font="simple"))

   # === Simple Font ===
   #  *   **  ** *** ***  ** *** *   *
   # * * *   *    *   *  *   *   **  *
   # ***  *  *    *   *  * * **  * * *
   # * *   * *    *   *  * * *   *  **
   # * * **   ** *** ***  ** *** *   *

   print("\n=== Block Font ===")
   print(asciigenator.generate("Ishan", font="block"))

   # === Block Font ===
   #   █
   #  █ █  ████  ████ █████ █████  ████ █████  █   █
   #  █ █  █     █       █     █   █     █     ██  █
   # █████  ███  █       █     █   █  ██ ████  █ █ █
   # █   █     █ █       █     █   █   █ █     █  ██
   # █   █ ████   ████ █████ █████  ████ █████ █   █

   print("\n=== Available Fonts ===")
   print(asciigenator.list_fonts())

   # === Available Fonts ===
   # ['block', 'simple']


Command Line Usage
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   asciigenator "Hello World"
   asciigenator "Hello World" --font block
   asciigenator --list-fonts
   asciigenator "Hello World" --font block  --border "#"
   asciigenator "Hello World"  --font block --color magenta
