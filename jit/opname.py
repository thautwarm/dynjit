import opcode
POP_TOP = opcode.opmap['POP_TOP']
ROT_TWO = opcode.opmap['ROT_TWO']
ROT_THREE = opcode.opmap['ROT_THREE']
DUP_TOP = opcode.opmap['DUP_TOP']
DUP_TOP_TWO = opcode.opmap['DUP_TOP_TWO']
ROT_FOUR = opcode.opmap['ROT_FOUR']
NOP = opcode.opmap['NOP']
UNARY_POSITIVE = opcode.opmap['UNARY_POSITIVE']
UNARY_NEGATIVE = opcode.opmap['UNARY_NEGATIVE']
UNARY_NOT = opcode.opmap['UNARY_NOT']
UNARY_INVERT = opcode.opmap['UNARY_INVERT']
BINARY_MATRIX_MULTIPLY = opcode.opmap['BINARY_MATRIX_MULTIPLY']
INPLACE_MATRIX_MULTIPLY = opcode.opmap['INPLACE_MATRIX_MULTIPLY']
BINARY_POWER = opcode.opmap['BINARY_POWER']
BINARY_MULTIPLY = opcode.opmap['BINARY_MULTIPLY']
BINARY_MODULO = opcode.opmap['BINARY_MODULO']
BINARY_ADD = opcode.opmap['BINARY_ADD']
BINARY_SUBTRACT = opcode.opmap['BINARY_SUBTRACT']
BINARY_SUBSCR = opcode.opmap['BINARY_SUBSCR']
BINARY_FLOOR_DIVIDE = opcode.opmap['BINARY_FLOOR_DIVIDE']
BINARY_TRUE_DIVIDE = opcode.opmap['BINARY_TRUE_DIVIDE']
INPLACE_FLOOR_DIVIDE = opcode.opmap['INPLACE_FLOOR_DIVIDE']
INPLACE_TRUE_DIVIDE = opcode.opmap['INPLACE_TRUE_DIVIDE']
GET_AITER = opcode.opmap['GET_AITER']
GET_ANEXT = opcode.opmap['GET_ANEXT']
BEFORE_ASYNC_WITH = opcode.opmap['BEFORE_ASYNC_WITH']
BEGIN_FINALLY = opcode.opmap['BEGIN_FINALLY']
END_ASYNC_FOR = opcode.opmap['END_ASYNC_FOR']
INPLACE_ADD = opcode.opmap['INPLACE_ADD']
INPLACE_SUBTRACT = opcode.opmap['INPLACE_SUBTRACT']
INPLACE_MULTIPLY = opcode.opmap['INPLACE_MULTIPLY']
INPLACE_MODULO = opcode.opmap['INPLACE_MODULO']
STORE_SUBSCR = opcode.opmap['STORE_SUBSCR']
DELETE_SUBSCR = opcode.opmap['DELETE_SUBSCR']
BINARY_LSHIFT = opcode.opmap['BINARY_LSHIFT']
BINARY_RSHIFT = opcode.opmap['BINARY_RSHIFT']
BINARY_AND = opcode.opmap['BINARY_AND']
BINARY_XOR = opcode.opmap['BINARY_XOR']
BINARY_OR = opcode.opmap['BINARY_OR']
INPLACE_POWER = opcode.opmap['INPLACE_POWER']
GET_ITER = opcode.opmap['GET_ITER']
GET_YIELD_FROM_ITER = opcode.opmap['GET_YIELD_FROM_ITER']
PRINT_EXPR = opcode.opmap['PRINT_EXPR']
LOAD_BUILD_CLASS = opcode.opmap['LOAD_BUILD_CLASS']
YIELD_FROM = opcode.opmap['YIELD_FROM']
GET_AWAITABLE = opcode.opmap['GET_AWAITABLE']
INPLACE_LSHIFT = opcode.opmap['INPLACE_LSHIFT']
INPLACE_RSHIFT = opcode.opmap['INPLACE_RSHIFT']
INPLACE_AND = opcode.opmap['INPLACE_AND']
INPLACE_XOR = opcode.opmap['INPLACE_XOR']
INPLACE_OR = opcode.opmap['INPLACE_OR']
WITH_CLEANUP_START = opcode.opmap['WITH_CLEANUP_START']
WITH_CLEANUP_FINISH = opcode.opmap['WITH_CLEANUP_FINISH']
RETURN_VALUE = opcode.opmap['RETURN_VALUE']
IMPORT_STAR = opcode.opmap['IMPORT_STAR']
SETUP_ANNOTATIONS = opcode.opmap['SETUP_ANNOTATIONS']
YIELD_VALUE = opcode.opmap['YIELD_VALUE']
POP_BLOCK = opcode.opmap['POP_BLOCK']
END_FINALLY = opcode.opmap['END_FINALLY']
POP_EXCEPT = opcode.opmap['POP_EXCEPT']
STORE_NAME = opcode.opmap['STORE_NAME']
DELETE_NAME = opcode.opmap['DELETE_NAME']
UNPACK_SEQUENCE = opcode.opmap['UNPACK_SEQUENCE']
FOR_ITER = opcode.opmap['FOR_ITER']
UNPACK_EX = opcode.opmap['UNPACK_EX']
STORE_ATTR = opcode.opmap['STORE_ATTR']
DELETE_ATTR = opcode.opmap['DELETE_ATTR']
STORE_GLOBAL = opcode.opmap['STORE_GLOBAL']
DELETE_GLOBAL = opcode.opmap['DELETE_GLOBAL']
LOAD_CONST = opcode.opmap['LOAD_CONST']
LOAD_NAME = opcode.opmap['LOAD_NAME']
BUILD_TUPLE = opcode.opmap['BUILD_TUPLE']
BUILD_LIST = opcode.opmap['BUILD_LIST']
BUILD_SET = opcode.opmap['BUILD_SET']
BUILD_MAP = opcode.opmap['BUILD_MAP']
LOAD_ATTR = opcode.opmap['LOAD_ATTR']
COMPARE_OP = opcode.opmap['COMPARE_OP']
IMPORT_NAME = opcode.opmap['IMPORT_NAME']
IMPORT_FROM = opcode.opmap['IMPORT_FROM']
JUMP_FORWARD = opcode.opmap['JUMP_FORWARD']
JUMP_IF_FALSE_OR_POP = opcode.opmap['JUMP_IF_FALSE_OR_POP']
JUMP_IF_TRUE_OR_POP = opcode.opmap['JUMP_IF_TRUE_OR_POP']
JUMP_ABSOLUTE = opcode.opmap['JUMP_ABSOLUTE']
POP_JUMP_IF_FALSE = opcode.opmap['POP_JUMP_IF_FALSE']
POP_JUMP_IF_TRUE = opcode.opmap['POP_JUMP_IF_TRUE']
LOAD_GLOBAL = opcode.opmap['LOAD_GLOBAL']
SETUP_FINALLY = opcode.opmap['SETUP_FINALLY']
LOAD_FAST = opcode.opmap['LOAD_FAST']
STORE_FAST = opcode.opmap['STORE_FAST']
DELETE_FAST = opcode.opmap['DELETE_FAST']
RAISE_VARARGS = opcode.opmap['RAISE_VARARGS']
CALL_FUNCTION = opcode.opmap['CALL_FUNCTION']
MAKE_FUNCTION = opcode.opmap['MAKE_FUNCTION']
BUILD_SLICE = opcode.opmap['BUILD_SLICE']
LOAD_CLOSURE = opcode.opmap['LOAD_CLOSURE']
LOAD_DEREF = opcode.opmap['LOAD_DEREF']
STORE_DEREF = opcode.opmap['STORE_DEREF']
DELETE_DEREF = opcode.opmap['DELETE_DEREF']
CALL_FUNCTION_KW = opcode.opmap['CALL_FUNCTION_KW']
CALL_FUNCTION_EX = opcode.opmap['CALL_FUNCTION_EX']
SETUP_WITH = opcode.opmap['SETUP_WITH']
LIST_APPEND = opcode.opmap['LIST_APPEND']
SET_ADD = opcode.opmap['SET_ADD']
MAP_ADD = opcode.opmap['MAP_ADD']
LOAD_CLASSDEREF = opcode.opmap['LOAD_CLASSDEREF']
EXTENDED_ARG = opcode.opmap['EXTENDED_ARG']
BUILD_LIST_UNPACK = opcode.opmap['BUILD_LIST_UNPACK']
BUILD_MAP_UNPACK = opcode.opmap['BUILD_MAP_UNPACK']
BUILD_MAP_UNPACK_WITH_CALL = opcode.opmap['BUILD_MAP_UNPACK_WITH_CALL']
BUILD_TUPLE_UNPACK = opcode.opmap['BUILD_TUPLE_UNPACK']
BUILD_SET_UNPACK = opcode.opmap['BUILD_SET_UNPACK']
SETUP_ASYNC_WITH = opcode.opmap['SETUP_ASYNC_WITH']
FORMAT_VALUE = opcode.opmap['FORMAT_VALUE']
BUILD_CONST_KEY_MAP = opcode.opmap['BUILD_CONST_KEY_MAP']
BUILD_STRING = opcode.opmap['BUILD_STRING']
BUILD_TUPLE_UNPACK_WITH_CALL = opcode.opmap['BUILD_TUPLE_UNPACK_WITH_CALL']
LOAD_METHOD = opcode.opmap['LOAD_METHOD']
CALL_METHOD = opcode.opmap['CALL_METHOD']
CALL_FINALLY = opcode.opmap['CALL_FINALLY']
POP_FINALLY = opcode.opmap['POP_FINALLY']

