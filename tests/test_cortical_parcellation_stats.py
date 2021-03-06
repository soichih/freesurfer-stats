"""
freesurfer-stats, a Python Library to Read FreeSurfer's Cortical Parcellation Anatomical Statistics
Copyright (C) 2019 Fabian Peter Hammerle <fabian@hammerle.me>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import datetime
import os

import pandas.util.testing
import pytest

from conftest import SUBJECTS_DIR
from freesurfer_stats import CorticalParcellationStats


@pytest.mark.parametrize(
    ('path', 'headers', 'hemisphere',
     'whole_brain_measurements', 'structural_measurements'),
    [(os.path.join(SUBJECTS_DIR, 'fabian', 'stats', 'lh.aparc.DKTatlas.stats.short'),
      {'CreationTime': datetime.datetime(2019, 5, 9, 21, 5, 54, tzinfo=datetime.timezone.utc),
       'generating_program': 'mris_anatomical_stats',
       'cvs_version': 'Id: mris_anatomical_stats.c,v 1.79 2016/03/14 15:15:34 greve Exp',
       'mrisurf.c-cvs_version': 'Id: mrisurf.c,v 1.781.2.6 2016/12/27 16:47:14 zkaufman Exp',
       'cmdline': 'mris_anatomical_stats -th3 -mgz -cortex ../label/lh.cortex.label'
                  ' -f ../stats/lh.aparc.DKTatlas.stats -b -a ../label/lh.aparc.DKTatlas.annot'
                  ' -c ../label/aparc.annot.DKTatlas.ctab fabian lh white',
       'sysname': 'Linux',
       'hostname': 'another-hostname',
       'machine': 'x86_64',
       'user': 'some-username',
       'SUBJECTS_DIR': '/home/some-username/freesurfer-subjects',
       'anatomy_type': 'surface',
       'subjectname': 'fabian',
       'hemi': 'lh',
       'AnnotationFile': '../label/lh.aparc.DKTatlas.annot',
       'AnnotationFileTimeStamp': datetime.datetime(2019, 5, 9, 23, 5, 40)},
      'left',
      {'white_surface_total_area_mm^2': 98553,
       'mean_thickness_mm': 2.50462,
       'brain_segmentation_volume_mm^3': 1327432.000000,
       'brain_segmentation_volume_without_ventricles_mm^3': 1316285.000000,
       'brain_segmentation_volume_without_ventricles_from_surf_mm^3': 1315572.548920,
       'total_cortical_gray_matter_volume_mm^3': 553998.311189,
       'supratentorial_volume_mm^3': 1172669.548920,
       'supratentorial_volume_without_ventricles_mm^3': 1164180.548920,
       'estimated_total_intracranial_volume_mm^3': 1670487.274486},
      [{'structure_name': 'caudalanteriorcingulate',
        'number_of_vertices': 2061,
        'surface_area_mm^2': 1472,
        'gray_matter_volume_mm^3': 4258,
        'average_thickness_mm': 2.653,
        'thickness_stddev_mm': 0.644,
        'integrated_rectified_mean_curvature_mm^-1': 0.135,
        'integrated_rectified_gaussian_curvature_mm^-2': 0.020,
        'folding_index': 27,
        'intrinsic_curvature_index': 1.6},
       {'structure_name': 'caudalmiddlefrontal',
        'number_of_vertices': 4451,
        'surface_area_mm^2': 3039,
        'gray_matter_volume_mm^3': 8239,
        'average_thickness_mm': 2.456,
        'thickness_stddev_mm': 0.486,
        'integrated_rectified_mean_curvature_mm^-1': 0.116,
        'integrated_rectified_gaussian_curvature_mm^-2': 0.020,
        'folding_index': 42,
        'intrinsic_curvature_index': 3.7},
       {'structure_name': 'insula',
        'number_of_vertices': 3439,
        'surface_area_mm^2': 2304,
        'gray_matter_volume_mm^3': 7594,
        'average_thickness_mm': 3.193,
        'thickness_stddev_mm': 0.620,
        'integrated_rectified_mean_curvature_mm^-1': 0.116,
        'integrated_rectified_gaussian_curvature_mm^-2': 0.027,
        'folding_index': 33,
        'intrinsic_curvature_index': 3.5}]),
     (os.path.join(
         SUBJECTS_DIR, 'fabian', 'stats', 'rh.aparc.pial.stats.short'),
      {'CreationTime': datetime.datetime(2019, 5, 9, 21, 3, 42, tzinfo=datetime.timezone.utc),
       'generating_program': 'mris_anatomical_stats',
       'cvs_version': 'Id: mris_anatomical_stats.c,v 1.79 2016/03/14 15:15:34 greve Exp',
       'mrisurf.c-cvs_version': 'Id: mrisurf.c,v 1.781.2.6 2016/12/27 16:47:14 zkaufman Exp',
       'cmdline': 'mris_anatomical_stats -th3 -mgz -cortex ../label/rh.cortex.label'
                  ' -f ../stats/rh.aparc.pial.stats -b -a ../label/rh.aparc.annot'
                  ' -c ../label/aparc.annot.ctab fabian rh pial',
       'sysname': 'Linux',
       'hostname': 'some-hostname',
       'machine': 'x86_64',
       'user': 'some-username',
       'SUBJECTS_DIR': '/home/some-username/freesurfer-subjects',
       'anatomy_type': 'surface',
       'subjectname': 'fabian',
       'hemi': 'rh',
       'AnnotationFile': '../label/rh.aparc.annot',
       'AnnotationFileTimeStamp': datetime.datetime(2019, 5, 9, 22, 27, 28)},
      'right',
      {'pial_surface_total_area_mm^2': 121260,
       'mean_thickness_mm': 2.4817,
       'brain_segmentation_volume_mm^3': 1327432.000000,
       'brain_segmentation_volume_without_ventricles_mm^3': 1316285.000000,
       'brain_segmentation_volume_without_ventricles_from_surf_mm^3': 1315572.548920,
       'total_cortical_gray_matter_volume_mm^3': 553998.311189,
       'supratentorial_volume_mm^3': 1172669.548920,
       'supratentorial_volume_without_ventricles_mm^3': 1164180.548920,
       'estimated_total_intracranial_volume_mm^3': 1670487.274486},
      [{'structure_name': 'bankssts',
        'number_of_vertices': 1344,
        'surface_area_mm^2': 825,
        'gray_matter_volume_mm^3': 2171,
        'average_thickness_mm': 2.436,
        'thickness_stddev_mm': 0.381,
        'integrated_rectified_mean_curvature_mm^-1': 0.115,
        'integrated_rectified_gaussian_curvature_mm^-2': 0.028,
        'folding_index': 19,
        'intrinsic_curvature_index': 1.7},
       {'structure_name': 'transversetemporal',
        'number_of_vertices': 651,
        'surface_area_mm^2': 545,
        'gray_matter_volume_mm^3': 1061,
        'average_thickness_mm': 2.251,
        'thickness_stddev_mm': 0.317,
        'integrated_rectified_mean_curvature_mm^-1': 0.110,
        'integrated_rectified_gaussian_curvature_mm^-2': 0.021,
        'folding_index': 3,
        'intrinsic_curvature_index': 0.6}])],
)
def test_read(path, headers, hemisphere, whole_brain_measurements, structural_measurements):
    stats = CorticalParcellationStats.read(path)
    assert headers == stats.headers
    assert hemisphere == stats.hemisphere
    pandas.util.testing.assert_frame_equal(
        left=pandas.DataFrame([whole_brain_measurements]),
        right=stats.whole_brain_measurements,
        check_like=True,  # ignore the order of index & columns
        check_dtype=True,
        check_names=True,
    )
    assert list(stats.structural_measurements.columns) == [
        'structure_name',
        'number_of_vertices',
        'surface_area_mm^2',
        'gray_matter_volume_mm^3',
        'average_thickness_mm',
        'thickness_stddev_mm',
        'integrated_rectified_mean_curvature_mm^-1',
        'integrated_rectified_gaussian_curvature_mm^-2',
        'folding_index',
        'intrinsic_curvature_index',
    ]
    pandas.util.testing.assert_frame_equal(
        left=pandas.DataFrame(structural_measurements),
        right=stats.structural_measurements,
        check_like=True,  # ignore the order of index & columns
        check_dtype=True,
        check_names=True,
    )
