# Copyright 2020 Jiang Shenghu
# SPDX-License-Identifier: Apache-2.0
from .utils import filter_contains, slugify, sizeof
from .mode import Mode
from .isl import get_unnamed_tuples, get_named_tuples, \
    structure_named_fixed_box, structure_unnamed_fixed_box, map_out_constant_dim
from .tir import tir_imm, tir_store, tir_load, tir_cuda_shared_sync, tir_thread_extent_attr
from .autotune import load_best
from .sympy2isl import parse_sympy_to_isl_repr, constraints_to_isl_repr, ISLReprPrinter

cuda_settings = {
    'max_threads': 1024,
    'max_shared_memory': 48 * 1024,
}
