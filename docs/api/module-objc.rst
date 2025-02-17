:mod:`objc` -- The PyObjC bridge
================================

.. module:: objc
   :platform: macOS
   :synopsis: The PyObjC bridge

.. moduleauthor:: Ronald Oussoren <ronaldoussoren@mac.com>


Introduction
------------

The module :mod:`objc` is the core of PyObjC and provides the automatic
bridging between Python and Objective-C. It also provides a number of
utility functions and types that make it easier to integrate Python
and Objective-C code.

The module :mod:`objc` defines a number of functions whose names start with
an underscore. Those functions are private and should not be used, they can
be removed from release without warning.

NOTE: This document is currently mostly an exhaustive list of stuff and
needs to be reorganised once I've filled in the technical details.

Bridge options
..............

.. data:: options

   The object :data:`options` has attributes for reading and setting
   a number of configuration options for the bridge.

   Attributes whose names start with an underscore are reserved for
   use by the bridge and can appear or disappear with every release
   of PyObjC.

   .. versionadded:: 3.0


   .. data:: objc.options.verbose

      When the value is :const:`True` the bridge will log more information.

      This currently results in output on the standard error stream whenever
      an exception is translated from Python to Objective-C.

   .. data:: objc.options.use_kvo

      The default value for the *__useKVO__* attribute on
      classes.

      When the *__useKVO__* attribute of a class is true instances
      of the class will generate Key-Value Observation notifications when
      setting attributes from Python.


   .. data:: objc.options.unknown_pointer_raises

      When True (the default) the bridge will raise an exception when
      it encounters a pointer value that cannot be converted to Python,
      otherwise it it creates instances of :class:`ObjCPointer`.

   .. data:: objc.options.strbridge_enabled

      Python 2 only: When True (the default) instances of :class:`str`
      are bridged as instances of a subclass of *NSString*, otherwise
      strings are not bridged.

      .. note::

         This option is only relevant for Python 2.x, for Python 3.x
         instances of :class:`str` are bridged as instances of a
         subclass of *NSString* and instances of :class:`bytes` (
         the :class:`str` class in Python 2) are bridged as instances
         of a subclass of *NSData*.

   .. data:: objc.options.deprecation_warnings

      When 0 (the default) the bridge will not emit deprecation warnings,
      otherwise the value should be one of the :data:`MAC_OS_X_VERSION_10_N`
      constants and the bridge will emit a deprecation warning for APIs
      that were deprecated in the SDK (or earlier).

      Deprecation warnings are emitted using the :mod:`warnings` module,
      using the warning :class:`objc.ApiDeprecationWarning`.

      .. versionadded:: 3.3

  .. data:: objc.options.structs_indexable

     When True (the default) PyObjC's wrappers for C structs can be indexed
     as if they are (writable) tuples. When False this isn't possible.

     .. note:: This is primarily an experimental option, that will likely be removed in a future version.

  .. data:: objc.options.structs_writable

     When True (the default) PyObjC's wrappers for C structs are writable,
     otherwise they are read-only.

     .. note:: This is an experimental option. I don't know yet if making structs read-only will be a better.


Deprecated functions for changing options
.........................................

.. function:: setVerbose(yesOrNo)

   When the argument is :const:`True` the bridge will log more information.

   This currently results in output on the standard error stream whenever
   an exception is translated from Python to Objective-C.

   .. deprecated:: 3.0 Use :data:`objc.options` instead


.. function:: getVerbose()

   Returns the current value of the verbose flag.

   .. deprecated:: 3.0 Use :data:`objc.options` instead


.. function:: setUseKVOForSetattr

   Sets the default value for the *__useKVO__* attribute on
   classes defined after this call. Returns the previous value.

   When the *__useKVO__* attribute of a class is true instances
   of the class will generate Key-Value Observation notifications when
   setting attributes from Python.

   .. deprecated:: 3.0 Use :data:`objc.options` instead

.. function:: setStrBridgeEnabled(yesOrNo)

   If *yesOrNo* is true instances of :class:`str` are bridged
   as NSString instances, otherwise bridging issues a :data:`PyObjCStrBridgeWarning`
   warning and still bridges as an NSString instances.

   By default PyObjC behaves as if ``setStrBridgeEnabled(True)`` was called.

   .. note::

      This function is not available in Python 3.x

   .. note::

      Setting this option to false is discouraged and is mostly useful when porting
      to Python 3.

   .. deprecated:: 3.0 Use :data:`objc.options` instead


.. function:: getStrBridgeEnabled

   Returns :data:`True` if the str bridge is enabled and :data:`False` when it is
   not.

   .. note::

      This function is not available in Python 3.x

   .. deprecated:: 3.0 Use :data:`objc.options` instead

Weak references
---------------


.. class:: WeakRef(object)

   It is not possible to use the :mod:`weakref` module to create
   weak references to Cocoa objects due to implementation restrictions
   (at best it would be possible to create a weakref to the Python
   proxy for such objects).

   PyObjC implements a zero-ing weakref object when running on
   macOS 10.7 or later. These objects more or less behave the
   same as ``__weak`` variables in Objective-C.

   The *object* must be a Cocoa object, and must not be a CoreFoundation
   object (unless the CoreFoundation type is transparently bridged to Cocoa).

   .. versionadded: 3.0

   .. method:: __call__()

      Returns the weakly references object when that is still alive,
      otherwise returns :data:`None`.

    .. note::

       Unlike :class:`weakref.ref` this class cannot be subclasses, and
       does not have a callback option. The callback option cannot be
       reliably be implemented with the current Objective-C runtime API.

    .. warning::

       Some Cocoa classes do not support weak references, see Apple's
       documentation for more information. Creating a weak reference
       to instances of such classes can be a hard error (that is,
       the interpreter crashes, you won't get a nice exception).

Associated Objects
------------------

On macOS 10.6 or later the Objective-C runtime has an API for
associated objects, which are more or less additional instance variables
for objects.

.. function:: setAssociatedObject(object, key, value, policy)

   :param object: the base object (a Cocoa instance)
   :type key: an arbitrary object, the same object must be used to
               retrieve the value.
   :param value: value for the associated object
   :param policy: policy for the association (see below)

   Associate *assoc* with *object* under name *name*.

.. function:: getAssociatedObject(object, key)

   :param object: an object (a Cocoa instance)
   :param key: the key object that was used with :func:`setAssociatedObject`
   :return: the value for the key, or :data:`None`.

   Returns the value of an associated object.

.. function:: removeAssociatedObjects(object)

   :param object: an object (a Cocoa instance)

   Remove all associations for *object*. It is generally a bad idea to
   use this function, because other libraries might have set associations
   as well.

.. data:: OBJC_ASSOCIATION_ASSIGN

   Policy for creating a weak reference to the associated object

   .. note:: Don't use this when the value is a pure python object, unless
             you arrange to keep the proxy object alive some other way.

.. data:: OBJC_ASSOCIATION_RETAIN_NONATOMIC

   Policy for creating a strong reference to the associated object.

.. data:: OBJC_ASSOCIATION_COPY_NONATOMIC

   Policy for creating a strong reference to a copy of the associated object.

.. data:: OBJC_ASSOCIATION_RETAIN

   Policy for creating a strong reference to the associated object, the
   association is made atomically.

.. data:: OBJC_ASSOCIATION_COPY

   Policy for creating a strong reference to a copy of the associated object,
   the association is made atomically.

Utilities
---------

.. function:: macos_available(major, minor, patch=0)

   Returns true iff the current macOS version is at least the version
   specified. Use this like the "@available" construct in Objective-C.

.. function:: allocateBuffer(length)

   Returns a writable buffer object of *length* bytes. This function is
   equivalent to `bytearray(length)`

   .. deprecated: 8.2

.. function:: CFToObject

   Converts an object from the standard library :mod:`CF` module to a
   PyObjC wrapper for the same CoreFoundation object. Raises an exception
   when the conversion fails.

   .. deprecated:: 2.4
      part of support for the CF module in the python 2 std. library,
      will be removed in PyObjC 3.0.

   .. note::
      this function is not available for Python 3.


.. function:: ObjectToCF

   Converts a PyObjC wrapper for a CoreFoundation object to an object from the standard
   library :mod:`CF` module for the same CoreFoundation object. Raises an exception
   when the conversion fails.

   .. deprecated:: 2.4
      part of support for the CF module in the python 2 std. library,
      will be removed in PyObjC 3.0.

   .. note::
      this function is not available for Python 3.



Accessing classes and protocols
-------------------------------

.. function:: lookUpClass(classname)

   :param classname: the name of an Objective-C class
   :type classname: string
   :return: the named Objective-C class
   :raise: :exc:`objc.nosuchclass_error` when the class does not exist


.. function:: getClassList()

   :return: a list of a classes known to the Objective-C runtime


.. function:: protocolsForClass(cls)

   Returns a list of Protocol objects that the class claims to
   implement directly. The *cls* object must a subclass of NSObject.

.. function:: protocolsForProcess

   Returns a list of all Protocol objects known to the Objective-C
   runtime.

.. function:: propertiesForClass(objcClass)

   :type objcClass: an Objective-C class or formal protocol
   :return: a list of properties from the Objective-C runtime

   The return value is a list with information about
   properties on this class or protocol from the Objective-C runtime. This
   does not include properties superclasses.

   Every entry in the list is dictionary with the following keys:

   ============= =============================================================
   Key           Description
   ============= =============================================================
   *name*        Name of the property (a string)
   ------------- -------------------------------------------------------------
   *raw_attr*    Raw value of the attribute string (a byte string)
   ------------- -------------------------------------------------------------
   *typestr*     The type string for this attribute (a byte string)
   ------------- -------------------------------------------------------------
   *classname*   When the type string is ``objc._C_ID`` this is the
                 name of the Objective-C class (a string).
   ------------- -------------------------------------------------------------
   *readonly*    True iff the property is read-only (bool)
   ------------- -------------------------------------------------------------
   *copy*        True iff the property is copying the value (bool)
   ------------- -------------------------------------------------------------
   *retain*      True iff the property is retaining the value (bool)
   ------------- -------------------------------------------------------------
   *nonatomic*   True iff the property is not atomic (bool)
   ------------- -------------------------------------------------------------
   *dynamic*     True iff the property is dynamic (bool)
   ------------- -------------------------------------------------------------
   *weak*        True iff the property is weak (bool)
   ------------- -------------------------------------------------------------
   *collectable* True iff the property is collectable (bool)
   ------------- -------------------------------------------------------------
   *getter*      Non-standard selector for the getter method (a byte string)
   ------------- -------------------------------------------------------------
   *setter*      Non-standard selector for the setter method (a byte string)
   ============= =============================================================

   All values but *name* and *raw_attr* are optional. The other attributes
   contain a decoded version of the *raw_attr* value. The boolean attributes
   should be interpreted as :data:`False` when the aren't present.

   The documentation for the Objective-C runtime contains more information about
   property definitions.

   This function only returns information about properties as they are defined
   in the Objective-C runtime, that is using ``@property`` definitions in an
   Objective-C interface. Not all properties as they are commonly used  in
   Objective-C are defined using that syntax, especially properties in classes
   that were introduced before MacOSX 10.5.

   This function always returns an empty list on macOS 10.4.

   .. versionadded:: 2.3

.. function:: listInstanceVariables(classOrInstance)

   Returns a list of information about all instance variables for
   a class or instance. *ClassOrInstance* must be a subclass of NSObject,
   or an instance of such a class.

   The elements of the list are tuples with two elements: a string with
   the name of the instance variable and a byte string with the type encoding
   of the instance variable.

.. function:: getInstanceVariable(object, name)

   Returns the value of the instance variable *name*.

   .. warning::

      Direct access of instance variables should only be used as a debugging
      tool and could negatively affect the invariants that a class tries to
      maintain.

.. function:: setInstanceVariable(object, name, value[ ,updateRefCounts])

   Set the value of instance variable *name* to *value*. When the instance variable
   type encoding is :data:`objc._C_ID` *updateRefCounts* must be specified and tells
   whether or not the retainCount of the old and new values are updated.

   .. warning::

      Direct access of instance variables should only be used as a debugging
      tool and could negatively affect the invariants that a class tries to
      maintain.

   .. warning::

      It is very easy to introduce memory corruption when  *updateRefCounts* is false.
      In particular the caller of this method must ensure that the Objective-C
      representation of *value* is kept alive, when *value* is not a Cocoa object
      just keeping *value* alive isn't good enough.


.. function:: protocolNamed(name)

   Returns a Protocol object for the named protocol. Raises :exc:`ProtocolError`
   when the protocol does not exist.

   This is the equivalent of ``@protocol(name)`` in Objective-C.

.. exception:: ProtocolError

   Raised by :func:`protocolNamed` when looking up a protocol that does not
   exist.


Dynamic modification of classes
-------------------------------

.. function:: classAddMethods(cls, methods)

   Add a sequence of methods to the given class.

   The effect is simular to how categories work in Objective-C. If the class
   already implements a method that is defined in *methods* the existing
   implementation is replaced by the new one.

   The objects in *methods* should be one of:

   * :class:`selector` instances with a callable (that is, the first argument
     to :class:`selector` must not be :data:`None`).

   * :class:`classmethod` or :class:`staticmethod` instances that wrap a
     function object.

   * functions

   * unbound methods

   For the last two the method selector is calculated using the regular
   algorithm for this (e.g. as if ``selector(item)`` was called). The last
   two are instance methods by default, but automatically made class methods
   when the class (or a superclass) has a class method with the same
   selector.

.. function:: classAddMethod(cls, name, method)

   Adds function *method* as selector *name* to the given class. When *method*
   is a selector the signature and class-method-ness are copied from the selector.

   .. note::

      Adding a selector that's defined in Objective-C to another class will raise
      an exception.

.. class:: Category

   A helper class for adding a category to an existing Objecive-C class (subclass
   of *NSObject*).

   Usage::

       class NSObject (Category(NSObject)):
          def method(self):
              pass

   The metaclass uses :func:`classAddMethods` to add the methods in the category
   body to the base class.

   The name of the class must be the same as the argument to :class:`Category`.

   This will only add new methods to existing Objective-C classes, it is in
   particular not possible to add new members/slots to existing classes.


Plugin bundles
--------------

.. function:: currentBundle

   During module initialization this function returns an NSBundle object for
   the current bundle. This works for application as well as plug-ins created
   using `py2app <https://pythonhosted.org/py2app/>`_.

   After module initialization use ``NSBundle.bundleForClass_(ClassInYourBundle)``
   to get the bundle.

Memory management
-----------------

PyObjC automatically manages Cocoa reference counts for you, the functions
in this section help in finetuning this behaviour.

.. function:: recycleAutoreleasePool()

   Flush the NSAutoreleasePool that PyObjC creates on import. Use this
   before entering the application main loop when you do a lot of work
   before starting the main loop.

.. function:: removeAutoreleasePool()

   Use this in plugin bundles to remove the release pool that PyObjC creates
   on import. In plugins this pool will interact in unwanted ways with the
   embedding application.


.. function:: autorelease_pool()

   A context manager that runs the body of the block with a fresh autorelease
   pool. The actual release pool is not accessible.

   Usage::

        with autorelease_pool():
            pass

   .. todo:: insert links to documentation explaining why you'd want to use this.

Test support
------------

The functions in this section are present as support code for PyObjC's
unittests and are not part of the stable API. Please let us know if you
use these functions in your code.

.. function:: splitSignature(typestring)

   Split an encoded Objective-C signature string into the
   encoding strings for separate types.

   :param typestring: an encoded method signature (byte string)
   :return: list of type signatures
   :type typestring: byte string
   :rtype: list of byte strings


.. function:: splitStructSignature(typestring)

   Returns (structname, fields). *Structname* is a string or :data:`None` and
   *fields* is a list of (name, typestr) values. The *name* is a string or
   :data:`None` and the *typestr* is a byte string.

   Raises :exc:`ValueError` when the type is not the type string for a struct
   type.


.. function:: repythonify(object [, type])

   Internal API for converting an object to a given Objetive-C type
   and converting it back again.


Framework wrappers
------------------

.. function:: pyobjc_id(obj)

   Returns the address of the underlying object as an integer.

   .. note::

      This is basically the same as :func:`id`, but for the Objective-C
      object wrapped by PyObjC instead of python objects.



Types
-----

.. class:: objc_class

   This class is the metatype for Objective-C classes and provides no user-visible
   behavior.

.. class:: objc_object([cobject, [c_void_p]])

   This class is the root class for Objective-C classes, that is all wrappers for
   Objective-C classes are a subclass of this class. It is not possible to instantiate
   instances of Objective-C classes by using the class as a callable, instances are
   created using the standard Objective-C mechanisms instead.

   The *cobject* and *c_void_p* arguments should always be passed as keyword arguments,
   and at most one of them should be provided. This will construct a proxy object of the
   right subclass of :class:`objc_object` for the Cocoa object that the passed in value
   refers to. *Cobject* should be a Pytho capsule created using the :meth:`__cobject__`
   method, *c_void_p* should be a :class:`ctypes.c_void_p`.

   .. note::

      The normal way to create instances of (subclasses of) :class:`objc_object` is
      to call the normal Cocoa allocation method. Calling the class should only be used
      to construct a proxy from a pre-existing pointer value (for interoperability with
      other libraries).



   .. data:: pyobjc_ISA

      Read-only property that returns the current Objective-C classes of an object.

   .. data:: pyobjc_instanceMethods

      Read-only property that provides explicit access to just the instance methods
      of an object.

   .. data:: \__block_signature__

      Property with the type signature for calling a block, or :data:`None`.

   .. method:: __cobject__()

      Returns a capsule object with identifier "objc.__object__" and the a reference
      to the Objective-C object as the value.

   .. method:: __c_void_p__()

      Returns a :class:`ctypes.c_void_p` instance for this object.

   .. method:: __reduce__()

      This method ensures that Objective-C objects will not be pickled unless the subclass
      explicitly implements the pickle protocol. This is needed because the pickle will
      write an incomplete serialization of Objective-C objects for protocol 2 or later.

   .. method:: __class_getitem__(*args)
      :classmethod:

      Return an object representing the specialization of a generic class by type arguments found in key.

      .. note::

         This feature requires Python 3.9 or later.

   .. note::

      The wrapper classes for the *NSString* class cluster aren't subclasses
      of :class:`objc_object`, but are subclasses of the builtin :class:`unicode` type
      (:class:`str:` in Python 3).

.. class:: pyobjc_unicode

   This class is used to wrap instances of the *NSString* class cluster and is
   a subclass of the builtin Unicode type (:class:`unicode` for python 2 and :class:`str`
   for Python 3).

   Methods of the underlying *NSString* class can be accessed at as methods
   of the python type, unless they have the same name as a method of the built-in Unicode
   type.

   .. method:: nsstring

      Returns an instance of a subclass of :class:`objc_object` that represents the
      string. This provides full access to the Cocoa string API, but without easy
      interoperability with Python APIs.

   .. note::

      Instances of *NSString* can be mutable. Mutations to mutable Cocoa
      strings are not reflected in instances of :class:`pyobjc_unicode`, use
      :meth:`nsstring` and explicit conversion to the built-in unicode type when
      you work with mutable *NSString* values.

   .. note::

      Cocoa strings are wrapped using a subclass of the built-in unicode string
      to get better interaction between Python and Cocoa. Because Cocoa strings are
      instances of the built-in unicode type they can be passed to functions in
      extension modules that expect unicode arguments (in particular the file
      system access APIs such as :func:`open`).


.. class:: selector(function[, selector[, signature[, isClassMethod[, returnType[, argumentTypes[, isRequired]]]]]])

   This type is used to represent an Objective-C method.

   :param function:  The Python callable that is used for the method. Can be a :class:`classmethod` , but not a :class:`staticmethod`.
   :param selector:  The Objective-C selector for the method. The default is calculated from the \__name__ attribute for *function*
   :param signature: The type encoding for the method, the default signature assumes that all arguments and the result are objects
                     (or 'void' when the function does not contain a return statement with a value).
   :param isClassMethod: Used to specify if a method is a class method (default is :data:`True` if *function* is a :class:`classmethod`
                     and :data:`False` otherwise)
   :param isRequired:    Specify if the method is required (defaults to :data:`True`), used in the definition of protocols.

   .. data:: callable

      Read-only property with access to the underlying callable (the *function* argument to the constructor).

   .. data:: __doc__

      Documentation string for the selector

   .. data:: __signature__

      An :class:`inspect.Signature` for the object

      .. versionadded:: 3.0

      .. note::

         Only available for Python 3.3 or later.

   .. method:: __metadata__

      Returns a copy of the metadata dictionary for the selector.  See the
      :doc:`metadata system documentation </metadata/manual>` for more information.

.. class:: python_method(callable)


   Use this as a decorator in a Cocoa class definition to avoid creating a
   selector object for a method.

   This is used to add "normal" python methods to a class that's inheriting
   from a Cocoa class and makes it possible to use normal Python idioms in
   the part of the class that does not have to interact with the Objective-C
   world.

   For example::

       class MyClass (NSObject):

          @python_method
          @classmethod
          def fromkeys(self, keys):
              pass

          @python_method
          def items(self):
              pass

   In this example class *MyClass* has a Python classmethod "fromkeys" and
   a normal method "items", neither of which are converted to a selector object
   and neither of which are registered with the Objective-C runtime.

   Instances of this type have an attribute named *callable* containing the wrapped
   callable, but are themselves not callable.

   .. versionadded:: 3.0

   .. note::

      If you use multiple decorators the :class:`python_method` decorator should be
      the outermost decorator (that is, the first one in the list of decorators).

.. class:: ivar([name[, type[, isOutlet]]])

   Creates a descriptor for accessing an Objective-C instance variable. This should only
   be used in the definition of an Objective-C subclass, the bridge will use this information
   to create an instance variable with the same name on the Objective-C class itself.

   :param name: Name of the instance variable. The name defaults to the name the instance
                variable is bound to in a class definition.

   :param type: Type encoding for the instance varialble. Defaults to :data:`_C_ID` (that is,
                an object)

   :param isOutlet: If :data:`True` the instance variable is used as an outlet, by default
                the instance variable is not an outlet.

   .. note::
      Sharing an ivar object between multiple class definitions is not supported.


   Instances of :class:`ivar` have a number of attributes that help with introspection:

   * *__typestr__*: The type encoding of the Objective-C type of the variable. See
     :ref:`type-encodings` for more information.

   * *__name__*: The Objective-C name of the variable

   * *__isOutlet__*: :data:`True` if the variable is an :func:`IBOutlet`

   * *__isSlot__*: :data:`True` if the variable is a Python slot.


   The :class:`ivar` has convenience class methods for creating :class:`ivar` objects
   for specific C types:

   .. method:: bool([name])

      Create an instance variable that stores a value of C type ``bool``. See the
      class description for a description of the *name* argument.

   .. method:: char([name])

      Create an instance variable that stores a value of C type ``char``. See the
      class description for a description of the *name* argument. In general it
      is better to use :meth:`char_text` or :meth:`char_int`.

   .. method:: int([name])

      Create an instance variable that stores a value of C type ``int``. See the
      class description for a description of the *name* argument.

   .. method:: short([name])

      Create an instance variable that stores a value of C type ``short``. See the
      class description for a description of the *name* argument.

   .. method:: long([name])

      Create an instance variable that stores a value of C type ``long``. See the
      class description for a description of the *name* argument.

   .. method:: long_long([name])

      Create an instance variable that stores a value of C type ``long long``. See the
      class description for a description of the *name* argument.

   .. method:: unsigned_char([name])

      Create an instance variable that stores a value of C type ``unsigned char``. See the
      class description for a description of the *name* argument.

   .. method:: unsigned_int([name])

      Create an instance variable that stores a value of C type ``unsigned int``. See the
      class description for a description of the *name* argument.

   .. method:: unsigned_short([name])

      Create an instance variable that stores a value of C type ``unsigned short``. See the
      class description for a description of the *name* argument.

   .. method:: unsigned_long([name])

      Create an instance variable that stores a value of C type ``unsigned long``. See the
      class description for a description of the *name* argument.

   .. method:: unsigned_long_long([name])

      Create an instance variable that stores a value of C type ``unsigned long long``. See the
      class description for a description of the *name* argument.

   .. method:: float([name])

      Create an instance variable that stores a value of C type ``float``. See the
      class description for a description of the *name* argument.

   .. method:: double([name])

      Create an instance variable that stores a value of C type ``double``. See the
      class description for a description of the *name* argument.

   .. method:: BOOL([name])

      Create an instance variable that stores a value of C type ``BOOL``. See the
      class description for a description of the *name* argument.

   .. method:: UniChar([name])

      Create an instance variable that stores a value of C type ``UniChar``. See the
      class description for a description of the *name* argument. Values are
      (unicode) strings of length 1.

   .. method:: char_text([name])

      Create an instance variable that stores a value of C type ``char``. See the
      class description for a description of the *name* argument. Values are
      byte-strings of length 1.

   .. method:: char_int([name])

      Create an instance variable that stores a value of C type ``char``. See the
      class description for a description of the *name* argument. Values are
      integers in the range of a ``signed char`` in C.

   Framework bindings introduce new class methods for creating instance variables whose type
   is a particular C struct, as an example the Foundation bindings introduce a class method
   named ``NSRange`` with the same signature as the methods mentioned earlier.

   .. note::

      You cannot access these attributes  through an Objective-C instance, you have to access
      them through the class object. That's because :class:`ivar` is a data descriptor.

   .. seealso::

      Function :func:`IBOutlet`
         Definition of outlets.


.. class:: informal_protocol(name, selector_list)

   This class is used to specify which methods are part of an informal protocol
   in Objective-C. Informal protocols are a documentation construct in Objective-C and
   as such are not present in the Objective-C runtime (as opposed to formal protocols).

   Informal protocols are used by the bridge to automatically update method signatures when
   a class appears to implement an informal protocol. This makes it possible the define
   a large subset of Cocoa functionality without manually setting method signatures.

   :param name: Name of the protocol
   :param selector_list: A sequence of :class:`selector` instances, all of which should have no callable.

   .. data:: __name__

      Read-only property with the protocol name

   .. data:: selectors

      Read-only property with the sequence of selectors for this protocol


.. class:: formal_protocol(name, supers, selector_list)

   This class is used to represent formal protocols in Python, and is comparabile with the
   "@protocol" construct in Objective-C.

   :param name:     The name of the protocol
   :param supers:   A list of protocols this protocol inherits from
   :param selector_list: A sequence of :class:`selector` instances, all of which should have no callable.

   .. note::

      Constructing new protocols is supported on a subset of macOS platforms:

      * All 32-bit programs

      * 64-bit programs starting from macOS 10.7, but only when PyObjC was build with
        the 10.7 SDK (or later)

   .. note::

      The protocols created by PyObjC are not compatible with NSXPCInterface because that
      class needs information ("extended method signature") that cannot be registered through
      the public API for the Objective-C runtime. See :doc:`../notes/using-nsxpcinterface` for
      more information.

   .. data:: __name__

      Read-only property with the name of the protocol

   .. method:: name

      Returns the name of the protocol

   .. method:: conformsTo_(proto)

      Returns :data:`True` if this protocol conforms to protocol *proto*, returns :data:`False` otherwise.

   .. method:: descriptionForInstanceMethod_(selector)

      Returns a tuple with 2 byte strings: the selector name and the type signature for the selector.

      Returns :data:`None` when the selector is not part of the protocol.

   .. method:: descriptionForClassMethod_(selector)

      Returns a tuple with 2 byte strings: the selector name and the type signature for the selector.

      Returns :data:`None` when the selector is not part of the protocol.

   .. method:: instanceMethods()

      Returns a list of instance methods in this protocol.

   .. method:: classMethods()

      Returns a list of instance methods in this protocol.

   .. note::

      The interface of this class gives the impression that a protocol instance is an Objective-C
      object. That was true in earlier versions of macOS, but not in more recent versions.


.. class:: varlist

   A C array of unspecified length. Instances of this type cannot be created in Python code.

   This type is used when the API does not specify the amount of items in an array in a way
   that is usable by the bridge.

   .. warning::

      Access through a :class:`varlist` object can easily read or write beyond the end
      of the wrapped C array.  Read the Apple documentation for APIs that return a
      varlist to determine how many elements you can safely access and whether or not the
      array is mutable.

      The C array might also be freed by C code before the :class:`varlist` instance
      is garbage collected. The Apple documentation for the API should mention how long
      the reference is safe to use.

   .. data:: __typestr__

      The type encoding for elements of the array. See :ref:`type-encodings` for more
      information.

   .. method:: as_tuple(count)

      Returns a tuple containing the first *count* elements of the array.

   .. method:: as_buffer(count)

      Returns a writable :class:`memoryview` referencing the memory for the first *count*
      elements of the array.

      .. note::

         The returned :class:`memoryview` is currently always a byte view, future
         versions might return a view with a *format* attribute that's appropriate
         for the :data:`__typestr__` of the varlist object.

   .. method:: __getitem__(index)

      Returns the value of the *index*-th element of the array. Supports numeric
      indexes as well as slices with step 1 and a specified stop index.

      Negative indexes are not supported because these objects have an unspecified length.

   .. method:: __setitem__(index, value)

      Sets the value of the *index*-th element of the array. Supports numeric
      indexes as well as slices with step 1 and a specified stop index  (but assigning
      to a slice is only possible when that does not resize the array).

      Negative indexes are not supported because these objects have an unspecified length.

      .. warning::

         When underlying data type is :data:`objc._C_ID` (that is, an array of Cocoa
         objects it is very likely that the retain count of the object needs to be
         adjusted. The :meth:`__setitem__` method stores a reference to the object
         *without* adjusting any reference counts.

         The correct behavior depends on the kind of array used, when the array is
         documented as containing strong references you should increase the retain count
         of the new value and lower the retain of the old value (in that order).


.. class:: function

   Instances of this class represent global functions from Cocoa frameworks. These
   objects are created using :func:`loadBundleFunctions` and :func:`loadFunctionList`.

   .. data:: __doc__

      Read-only property with the documentation string for the function.

   .. data:: __name__

      Read-only property with the name of the function

   .. data:: __module__

      Read-write property with the module that defined the function

   .. data:: __signature__

      An :class:`inspect.Signature` for the object

      .. versionadded:: 3.0

      .. note::

         Only available for Python 3.3 or later.

   .. method:: __metadata__

      Returns a copy of the metadata dictionary for the selector.  See the
      :doc:`metadata system documentation </metadata/manual>` for more information.


.. class:: IMP

   This class is used to represent the actual implementation of an Objective-C
   method (basically a C function). Instances behave the same as unbound methods:
   you can call them but need to specify the "self" argument.

   .. data:: isAlloc

      Read-only attribute that specifies if the IMP is an allocator (that is,
      the implementation of "+alloc" or one of its variant)

   .. data:: isClassMethod

      Read-only attribute that specified if the IMP is for a class method.

   .. data:: signature

      Read-only attribute with the type encoding for the IMP.

   .. data:: selector

      Read-only attribute with the selector for the method that this IMP
      is associated with.

   .. data:: __name__

      Alias for :data:`selector`.

   .. data:: __signature__

      An :class:`inspect.Signature` for the object

      .. versionadded:: 3.0

      .. note::

         Only available for Python 3.3 or later.

   .. method:: __metadata__

      Returns a copy of the metadata dictionary for the selector.  See the
      :doc:`metadata system documentation </metadata/manual>` for more information.


.. class:: super

   This is a subclass of :class:`super <__builtin__.super>` that works
   properly for Objective-C classes as well as regular Python classes.

   The regular :class:`super <__builtin__.super>` does *not* work correctly
   for Cocoa classes, the default function doesn't support custom attribute
   getters as used by PyObjC.


Constants
---------

.. data:: nil

   Alias for :const:`None`, for easier translation of existing Objective-C
   code.

.. data:: YES

   Alias for :const:`True`, for easier translation of existing Objective-C
   code.

.. data:: NO

   Alias for :const:`False`, for easier translation of existing Objective-C
   code.

.. data:: NULL

   Singleton that tells the bridge to pass a :c:data:`NULL` pointer as
   an argument when the (Objective-)C type of that argument is a pointer.

   This behavior of the bridge is slightly different from using :data:`None`:
   with :data:`None` the bridge will allocate some memory for output
   parameters and pass a pointer to that buffer, with :data:`NULL` the
   bridge will always pass a :c:data:`NULL` pointer.

.. data:: MAC_OS_X_VERSION_MAX_ALLOWED

   The value of :c:data:`MAC_OS_X_VERSION_MAX_ALLOWED` when PyObjC was
   compiled.

.. data:: MAC_OS_X_VERSION_MIN_REQUIRED

   The value of :c:data:`MAC_OS_X_VERSION_MIN_REQUIRED` when PyObjC was
   compiled.

.. data:: MAC_OS_X_VERSION_CURRENT

   The currently running macOS version in the same format as
   the various ``MAC_OS_X_VERSION_10_N`` constants.

   The intended use is with API availability checks, more or less like
   the ``@available`` construct in Objective-C, that is:

   .. sourcecode:: python

      if objc.MAC_OS_X_VERSION_CURRENT >= objc.MAC_OS_X_VERSION_10_14:
         # Use API introducted in macOS 10.14
         ...

      else:
         # Use fallback implementation
         ...

.. data:: PyObjC_BUILD_RELEASE

   The version number of the SDK used to build PyObjC, in the same format
   as :data:`MAC_OS_X_VERSION_10_N`

.. data:: MAC_OS_X_VERSION_10_N

   There are currently 6 constants of this form, for ``N`` from 1 to 10,
   and these have the same value as the Objective-C constant of the same
   name.

.. data:: platform

   This always has the value "MACOSX".


.. _type-encodings:

Objective-C type strings
------------------------

The Objective-C runtime and the PyObjC bridge represent the types of
instance variables and methods arguments and return values as a string
with a compact representation. The Python representation of that string is
a byte string (that is type :class:`bytes` in Python 3.x and :class:`str`
in Python 2.x).

Basic types
............

The representation for basic types is a single character, the table below
lists symbolic constants in the for those constants.

======================== =================================================
Name                     Objective-C type
======================== =================================================
:const:`_C_ID`           *id* (an Objective-C instance)
------------------------ -------------------------------------------------
:const:`_C_CLASS`        an Objective-C class
------------------------ -------------------------------------------------
:const:`_C_SEL`          a method selector
------------------------ -------------------------------------------------
:const:`_C_CHR`          *char*
------------------------ -------------------------------------------------
:const:`_C_UCHR`         *unsigned char*
------------------------ -------------------------------------------------
:const:`_C_SHT`          *short*
------------------------ -------------------------------------------------
:const:`_C_USHT`         *unsigned short*
------------------------ -------------------------------------------------
:const:`_C_BOOL`         *bool*  (or *_Bool*)
------------------------ -------------------------------------------------
:const:`_C_INT`          *int*
------------------------ -------------------------------------------------
:const:`_C_UINT`         *unsigned int*
------------------------ -------------------------------------------------
:const:`_C_LNG`          *long*
------------------------ -------------------------------------------------
:const:`_C_ULNG`         *unsigned long*
------------------------ -------------------------------------------------
:const:`_C_LNG_LNG`      *long long*
------------------------ -------------------------------------------------
:const:`_C_ULNG_LNG`     *unsigned long long*
------------------------ -------------------------------------------------
:const:`_C_FLT`          *float*
------------------------ -------------------------------------------------
:const:`_C_DBL`          *double*
------------------------ -------------------------------------------------
:const:`_C_VOID`         *void*
------------------------ -------------------------------------------------
:const:`_C_UNDEF`        "other" (such a function)
------------------------ -------------------------------------------------
:const:`_C_CHARPTR`      C string (*char**)
------------------------ -------------------------------------------------
:const:`_C_NSBOOL`       *BOOL*
------------------------ -------------------------------------------------
:const:`_C_UNICHAR`      *UniChar*
------------------------ -------------------------------------------------
:const:`_C_CHAR_AS_TEXT` *char* when uses as text or a byte array
------------------------ -------------------------------------------------
:const:`_C_CHAR_AS_INT`  *int8_t* (or *char* when
                         used as a number)
======================== =================================================

The values :const:`_C_NSBOOL`, :const:`_C_UNICHAR`, :const:`_C_CHAR_AS_TEXT`,
and :const:`_C_CHAR_AS_INT` are inventions of PyObjC and are not used in
the Objective-C runtime.

The value :const:`_C_NSBOOL` is deprecated as of PyObjC 9, use :const:`_C_BOOL`
instead. The two constants are treated exactly the same in PyObjC now that
the corresponding C types have the same representation (which wasn't true
for PowerPC).

Complex types
..............

More complex types can be represented using longer type strings:

* a pointer to some type is :const:`_C_PTR` followed by the type string
  of the pointed-to type.

* a bitfield in a structure is represented as :const:`_C_BFLD` followed
  by an integer with the number of bits.

  Note that PyObjC cannot convert bitfields at this time.

* a C structure is represented as :const:`_C_STRUCT_B` followed by the
  struct name, followed by :const:`'='`, followed by the encoded types of
  all fields followed by :const:`_C_STRUCT_E`. The field name (including the
  closing equals sign) is optional.

  Structures are assumed to have the default field alignment, although
  it is possible to use a custom alignment when creating a custom type
  for a struct using :func:`objc.createStructType`.


* a C union is represented as :const:`_C_UNION_B` followed by the
  struct name, followed by :const:`'='`, followed by the encoded types of
  all fields followed by :const:`_C_UNION_E`. The field name (including the
  closing equals sign) is optional.

  Note that PyObjC cannot convert C unions at this time.

* a C array is represented as :const:`_C_ARY_B` followed by an integer
  representing the number of items followed by the encoded element type,
  followed by :const:`_C_ARY_E`.

* The C construct 'const' is mapped to :const:`_C_CONST`, that is a
  *const char\** is represented as :const:`_C_CONST` + :const:`_C_CHARPTR`.

* A C vector or matrix type (e.g. ``vector_float3`` and ``matrix_float3x3``
  are represented as follows:

  - Vector: :const:`_C_VECTOR_B` *N* *type* :const:`_C_VECTOR_E`
  - Matrix: :const:`_C_VECTOR_B` *N* ``","`` *M* *type* :const:`_C_VECTOR_E`

  These representations are not supported in the Objective-C runtime, but are
  inventions by PyObjC. Because libffi does not support the corresponding
  C types these encodings are supported in limited subset of possible
  method signatures (basically only those signatures that are used by
  Apple system libraries).

Additional prefixes
...................

* :const:`_C_ATOMIC` can prefix any basic C type and denotes that the value
  should be accessed using atomic instructions.

  This value is currently ignored by PyObjC.

* :const:`_C_COMPLEX` can prefix any basic C type and denotes a C complex
  type.

  This value is currently not supported by PyObjC (and is not used
  in frameworks).

Additional annotations for method and function arguments
........................................................

Method arguments can have prefixes that closer describe their functionality.
Those prefixes are inherited from Distributed Objects are not used by the
Objective-C runtime, but are used by PyObjC.

* When a pointer argument is an input argument it is prefixed by
  :const:`_C_IN`.

* When a pointer argument is an output argument it is prefixed by
  :const:`_C_OUT`.

* When a pointer argument is an input and output argument it is prefixed
  by :const:`_C_INOUT`.

* Distributed objects uses the prefix :const:`_C_BYCOPY` to tell that a
  value should be copied to the other side instead of sending a proxy
  reference. This is not used by PyObjC.

* Distributed objects uses the prefix :const:`_C_ONEWAY` on the method return
  type to tell that the method result is not used and the caller should not
  wait for a result from the other side. This is not used by PyObjC.

When a pointer argument to a function prefixed by :const:`_C_IN`,
:const:`_C_OUT` or :const:`_C_INOUT` the bridge assumes that it is a pass by
reference argument (that is, a pointer to a single value), unless other
information is provided to the bridge.

The :const:`_C_IN`, :const:`_C_INOUT` and :const:`_C_OUT` encodings
correspond to the keyword ``in``, ``inout`` and ``out`` in Objective-C
code. This can be used to add the right information to the Objective-C
runtime without using :doc:`the metadata system </metadata/index>`. For
example:

.. sourcecode:: objective-c

   @interface OCSampleClass

   -(void)copyResourceOfName:(NSString*)name error:(out NSError**)error;

   @end

This tells the compiler that *error* is an output argument, which doesn't
affect code generation or compiler warnings but does result in :const:`_C_OUT`
being present in the type encoding for the argument.


Special encoded types
.....................

The table below shows constants for a number of C types that are used
in Cocoa but are not basic C types.

  ======================= ==============================
  Constant                Objective-C type
  ======================= ==============================
  :const:`_C_CFTYPEID`    *CFTypeID*
  ----------------------- ------------------------------
  :const:`_C_NSInteger`   *NSInteger*
  ----------------------- ------------------------------
  :const:`_C_NSUInteger`  *NSUInteger*
  ----------------------- ------------------------------
  :const:`_C_CFIndex`     *CFIndex*
  ----------------------- ------------------------------
  :const:`_C_CGFloat`     *CGFloat*
  ----------------------- ------------------------------
  :const:`_C_NSRange`     *NSRange*
  ----------------------- ------------------------------
  :const:`_C_CFRange`     *CFRange*
  ----------------------- ------------------------------
  :const:`_sockaddr_type` *struct sockaddr*
  ======================= ==============================

..versionadded:: 8.3

  _C_NSRange, _C_CFRange


Context pointers
----------------

A number of Objective-C APIs have one argument that is a context pointer,
which is a *void\**. In Objective-C your can pass a pointer to an
arbitrary value, in Python this must be an integer.

PyObjC provides a :data:`context` object that can be used to allocate
unique integers and map those to objects.

.. function:: context.register(value)

   Add a value to the context registry.

   :param value: An arbitrary object
   :return: A unique integer that's suitable to be used as a context pointer
            (the handle).

.. function:: context.unregister(value):

   Remove an object from the context registry, this object must be have
   been added to the registry before.

   :param value: An object in the context registry

.. function:: context.get(handle)

   Retrieve an object from the registry given the return value from
   :func:`context.register`.


Descriptors
-----------

.. function:: IBOutlet([name])

   Creates an instance variable that can be used as an outlet in
   Interface Builder. When the name is not specified the bridge will
   use the name from the class dictionary.

   The code block below defines an instance variable named "button" and
   makes that available as an outlet in Interface Builder.

   .. code-block:: python

      class SomeObject (NSObject):

          button = IBOutlet()

   .. note::

      The IBOutlet function is recognized by Interface Builder when it
      reads Python code.

.. function:: IBAction(function)

   Mark an method as an action for use in Interface Builder.  Raises
   :exc:`TypeError` when the argument is not a function.

   Usage:

   .. code-block:: python

      class SomeObject (NSObject):

         @IBAction
         def saveDocument_(self, sender):
             pass

   .. note::

      The IBOutlet decorator is recognized by Interface Builder when it
      reads Python code. Beyond that the decoerator has no effect.

.. function:: IBInspectable(prop)

   Mark a property as a value that can be introspected in IB.

   See `the Xcode documentation <https://developer.apple.com/library/ios/recipes/xcode_help-IB_objects_media/chapters/CreatingaLiveViewofaCustomObject.html>` for more information on this decorator.

.. function:: IB_DESIGNABLE(cls)

   Class decorator to tell IB that the class can be used in IB designs.

   See `the Xcode documentation <https://developer.apple.com/library/ios/recipes/xcode_help-IB_objects_media/chapters/CreatingaLiveViewofaCustomObject.html>` for more information on this decorator.

.. function:: instancemethod

   Explicitly mark a method as an instance method. Use this when
   PyObjC incorrectly deduced that a method should be a class method.

   Usage:

   .. code-block:: python

        class SomeObject (NSObject):

           @instancemethod
           def alloc(self):
               pass

   .. note::

      There is no function named *objc.classmethod*, use
      :func:`classmethod <__builtin__.classmethod>` to explicitly mark a function
      as a class method.


.. function:: accessor

   Use this decorator on the definition of accessor methods to ensure
   that it gets the right method signature in the Objective-C runtime.

   The conventions for accessor names that can be used with Key-Value Coding
   is described in the `Apple documentation for Key-Value Coding`_

   The table below describes the convention for methods for a property named '<property>',
   with a short description and notes. The `Apple documentation for Key-Value Coding`_
   contains more information.

   ================================================== =================================== =========================================
   Name                                               Description                         Notes
   ================================================== =================================== =========================================
   *property*                                         Getter for a basic property.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   is\ *Property*                                     Likewise, for a boolean             PyObjC won't automatically set the
                                                      property.                           correct property type, use
                                                                                          :func:`typeAccessor` instead of
                                                                                          :func:`accessor`.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   set\ *Property*\ _                                 Setter for a basic property
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   countOf\ *Property*                                Returns the number of
                                                      items in a indexed
                                                      property, or unordered
                                                      property
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   objectIn\ *Property*\ AtIndex\_                    Returns the object at a specific
                                                      index for an indexed property
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   *property*\ AtIndexes\_                            Returns an array of                 Don't use this with
                                                      object values at specific           :func:`typedAccessor`.
                                                      indexes for an indexed
                                                      property. The argument
                                                      is an *NSIndexSet*.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   get\ *Property*\ _range_                           Optimized accessor                  Not supported by PyObjC, don't use
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   insertObject_in\ *Property*\ AtIndex\_             Add an object to an indexed
                                                      property at a specific index.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   insert\ *Property*\ _atIndexes_                    Insert the values from a list of    Don't use this with
                                                      at specific indices. The            :func:`typedAccessor`.
                                                      arguments are an *NSArray*
                                                      and an *NSIndexSet*.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   removeObjectFrom\ *Property*\ AtIndex\_            Remove the value
                                                      at a specific index of an
                                                      indexed property.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   remove\ *Property*\ AtIndexes\_                    Remove the values at specific
                                                      indices of an indexed property. The
                                                      argument is an
                                                      *NSIndexSet*.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   replaceObjectIn\ *Property*\ AtIndex_withObject\_  Replace the value at a specific
                                                      index of an indexed property.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   replace\ *Property*\ AtIndexes_with\ *Property*\_  Replace the values at specific      Don't use with :func:`typedAccessor`
                                                      indices of an indexed property.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   enumeratorOf\ *Property*                            Returns an *NSEnumerator*
                                                       for an unordered property.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   memberOf\ *Property*\ _                             Returns True if the value is
                                                       a member of an unordered property
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   add\ *Property*\ Object\_                           Insert a specific object in
                                                       an unordered property.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   add\ *Property*\ _                                  Add a set of new values
                                                       to an unordered property.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   remove\ *Property*\ Object\_                        Remove an object
                                                       from an unordered property.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   remove\ *Property*\ _                               Remove a set of objects
                                                       from an unordered property.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   intersect\ *Property*\ _                            Remove all objects from
                                                       an unordered property that
                                                       are not in the set argument.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   validate\ *Property*\ _error_                       Validate the new value of a         For typed accessor's the value
                                                       property                            is wrapped in an *NSValue*
                                                                                           (but numbers and booleans are automatically
                                                                                           unwrapped by the bridge)
   ================================================== =================================== =========================================

   PyObjC provides another mechanism for defining properties: :class:`object_property`.

   .. versionchanged:: 2.5
      Added support for unordered properties. Also fixed some issues for 64-bit
      builds.

.. _`Apple documentation for Key-Value Coding`: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/SearchImplementation.html

.. function:: typedAccessor(valueType)

   Use this decorator on the definition of accessor methods to ensure
   that it gets the right method signature in the Objective-C runtime.

   The *valueType* is the encoded string for a single value.

   .. note::

      When you use a typed accessor you must also implement "setNilValueForKey\_",
      as described in the `Apple documentation for Key-Value Coding`_

.. function:: typedSelector(signature)

   Use this decorator to explicitly set the type signature for a method.

   An example:

   .. code-block:: python

        @typedSelector(b'I@:d')
        def makeUnsignedIntegerOfDouble_(self, d):
           return d


   .. versionchanged:: 8.3

      The decorated function can now also be a :func:`classmethod`

.. function:: namedSelector(name [, signature])

   Use this decorator to explicitly set the Objective-C method name instead
   of deducing it from the Python name. You can optionally set the method
   signature as well.

   .. versionchanged:: 8.3

      The decorated function can now also be a :func:`classmethod`

.. function:: callbackFor(callable[, argIndex=])

   Use this decorator to tell that this function is the callback for
   an (Objective-C) API that stores a reference to the callback
   function.

   You only *have* to use this API when the Objective-C API can store
   the callback function for later usage. For other functions the
   bridge can create a temporary callback stub.

   Using this decorator for methods is not supported

   Usage:

   .. code-block:: python

       @objc.callbackFor(NSArray.sortedArrayUsingFunction_context\_)
       def compare(left, right, context):
           return 1

   This tells the bridge that 'compare' is used as the sort function
   for NSArray, and ensures that the function will get the correct
   Objective-C signature.

   .. note::

      The example will also work without the decorator because
      NSArray won't store a reference to the compare function that
      is used after 'sortedArrayUsingFunction_context\_' returns.

.. function:: callbackPointer(closure)

   Returns a value that can be passed to a function expecting
   a ``void *`` argument. The value for *closure* must be a function
   that's decorated with :func:`callbackFor`.

   .. versionadded:: 3.1

.. function:: selectorFor(callable[, argIndex])

   Decorator to tell that this is the "callback" selector for another
   API.

   Usage:

   .. code-block:: python

      @objc.selectorFor(NSApplication.beginSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_)
      def sheetDidEnd_returnCode_contextInfo_(self, sheet, returnCode, info):
          pass

   This will tell the bridge that this method is used as the end method
   for a sheet API, and will ensure that the method is registered with
   the correct Objective-C signature.


.. function:: synthesize(name[, copy[, readwrite[, type[, ivarName]]]])

   :param name:  name of the property
   :param copy:  if false (default) values are stored as is, otherwise
                 new values are copied.
   :param readwrite: If true (default) the property is read-write
   :param type:  an encoded type for the property, defaults to
                 :data:`_C_ID`.
   :param iVarName: Name of the instance variable used to store
                    the value. Default to the name of the property
                    prefixed by and underscore.

   This synthensizes a getter, and if necessary, setter method with
   the correct signature. The getter and setter provide access to
   an instance variable.

   This can be used when specific semantics are required (such as
   copying values before storing them).

   The class :class:`object_property` provides simular features with
   a nicer python interface: with that class the property behaves
   itself like a property for python code, with this function you
   still have to call accessor methods in your code.

Interacting with ``@synchronized`` blocks
-----------------------------------------

PyObjC provides an API that implements locking in the same way as the
``@synchronized`` statement in Objective-C.

.. code-block:: python

  with object_lock(anNSObject):
      pass

.. class:: object_lock(value)

   This class represents the mutex that protects an Objective-C object
   for the ``@synchronized`` statement. This can be used as a context
   manager for the ``with`` statement, but can also be used standalone.

   .. method:: lock

      Acquire the object mutex

   .. method:: unlock

      Release the object mutex


Archiving Python and Objective-C objects
----------------------------------------

Python and Objective-C each provide a native object serialization method,
the :mod:`pickle` module in Python and the *NSCoding* protocol in Objective-C.

It is possible to use an *NSKeyedArchiver* to store any Python object that
can be pickled in an Objective-C serialized data object.

Due to technical details it is not possible to pickle an Objective-C object,
unless someone explicitly implements the pickle protocol for such an object.

Properties
----------

Introduction
............

Both Python and Objective-C have support for properties, which are object attributes
that are accessed using attribute access syntax but which result in a method call.

The Python built-in :class:`property <__builtin__.property__` is used to define new
properties in plain Python code. These properties don't full interoperate with
Objective-C code though because they do not necessarily implement the Objective-C
methods that mechanisms like Key-Value Coding use to interact with a class.

PyObjC therefore has a number of property classes that allow you to define new
properties that do interact fully with the Key-Value Coding and Observation
frameworks.

.. todo:: Implement method for enabling properties on existing classes and tell
   why that is off by default and when it will be turned on by default.

.. todo:: The description is way to minimal, even the design document contained
   more information.

.. class:: object_property(name=None, read_only=False, copy=False, dynamic=False, ivar=None, typestr=_C_ID, depends_on=None)


   :param name: Name of the property, the default is to extract the name from the class dictionary
   :param read_only: Is this a read-only property? The default is a read-write property.
   :param copy: Should the default setter method copy values? The default retains the new value without copying.
   :param dynamic: If this argument is :data:`True` the property will not generate default accessor,
     but will rely on some external process to create them.
   :param ivar: Name of the instance variable that's used to store the value. When this value is :data:`None`
     the name will be calculated from the property name. If it is :data:`NULL` there will be no instance variable.
   :param typestr: The Objective-C type for this property, defaults to an arbitrary object.
   :param depends_on: A sequence of names of properties the value of this property depends on.

During the class definition you can add accessor methods by using the property as a decorator


.. method:: object_property.getter

   Decorator for defining the getter method for a property. The name of the method should be the
   same as the property::

       class MyObject (NSObject):

           prop = objc.object_property()

           @prop.getter
           def prop(self):
              return 42


.. method:: object_property.setter

   Decorator for defining the setter method for a property. The name of the method should be the
   same as the property.


.. method:: object_property.validate

   Decorator for defining a Key-Value Coding validator for this property.


It is possible to override property accessor in a subclass::

   class MySubclass (MyObject):
       @MyObject.prop.getter
       def getter(self):
           return "the world"

This can also be used to convert a read-only property to a read-write one
by adding a setter accessor.


Properties for structured types
...............................

Key-Value Coding is slightly different for structured types like sets and
lists (ordered and unordered collections). For this reason PyObjC also provides
subclasses of :class:`object_property` that are tuned for these types.

.. class:: array_property

   This property implements a list-like property. When you access the property
   you will get an object that implements the :class:`MutableSequence` ABC, and
   that will generate the correct Key-Value Observation notifications when
   the datastructure is updated.

.. class:: set_property

   This property implements a set-like property. When you access the property
   you will get an object that implements the :class:`MutableSet` ABC, and
   that will generate the correct Key-Value Observation notifications when
   the datastructure is updated.

.. class:: dict_property

   This property is like an :class:`object_property`, but has an empty
   NSMutableDictionary object as its default value. This type is mostly
   provided to have a complete set of property types.

These collection properties are at this time experimental and do not yet
provide proper hooks for tweaking their behavior. Future versions of PyObjC
will provide such hooks (for example a method that will be called when an
item is inserted in an array property).


Unconvertable pointer values
----------------------------

With incomplete metadata the bridge can run into pointer values that
it cannot convert to normal Python values. When
:data:`options.unknown_pointer_raises <objc.options.unknown_pointer_raises>`
is false such pointer values are bridged as instances of :class:`ObjCPointer`.

The bridge will unconditionally emit a warning before creating such instances,
the reason for this is that the use of :class:`ObjCPointer` is unwanted
(that's why the creation of such objects is disabled by default in PyObjC 3.0).

.. class:: ObjCPointer

   .. data:: typestr

      A bytes string with the Objective-C type encoding for
      the pointed to value.

      .. versionadded: 8.5

   .. data:: pointerAsInteger

      An integer value with the raw pointer value.

"FILE*" support
---------------

.. class:: FILE

   This class is only present when using Python 3 and is used to
   represent "FILE*" handles in Python. For Python 2 the regular
   "file" type is used for that.

   This types provides a fairly limited file-like API for binary
   I/O. Instances of this type don't close the stream automatically and
   don't implement a contextmanager.

   .. method:: at_eof()

      Returns True iff the stream is at the EOF marker

   .. method:: has_errors()

      Return True iff the stream has errors.

   .. method:: close()

      Closes the stream.

   .. method:: flush()

      Flushes the file buffers.

      .. versionadded: 8.1

   .. method:: readline()

      Read a single line from the stream.

   .. method:: read(buffer_size)

      Read *buffer_size* bytes. This returns an empty bytes object
      when the stream has reached end-of-file.

   .. method:: write(buffer)

      Write *buffer* to the stream. Returns the number of bytes
      that are actually written.

   .. method:: tell()

      Returns the current offset of the stream.

   .. method:: seek(offset, whence)

      Seek to the specified offset.
