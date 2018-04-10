import xarray as xr
import numpy as np
from glob import glob
from multiprocessing import Pool
from os.path import join

def main():
    in_path = "/glade/scratch/dgagne/track_data_ncarstorm_3km_nc/"    
    out_path = "/glade/scratch/dgagne/track_data_ncarstorm_3km_nc_small/"
    sub_vars = ["p", "row", "col", "lon", "lat", "i", "j", "masks", "time",
                "track_id", "track_step", "RVORT1_MAX_curr", "REFL_COM_prev",
                "PSFC_prev", "T2_prev", "TD2_prev", "U10_prev", "V10_prev"]
    n_proc = 5
    pool = Pool(n_proc, maxtasksperchild=1)
    nc_files = sorted(glob(join(in_path, "*.nc")))
    for nc_file in nc_files:
        pool.apply_async(reduce_nc_file, (nc_file, sub_vars, out_path))
    pool.close()
    pool.join()

def reduce_nc_file(filename, sub_vars, out_path):
    file_end = filename.split("/")[-1]
    storm_obj = xr.open_dataset(filename)
    enc_dict = dict()
    for var in sub_vars:
        enc_dict[var] = {"zlib": True}
    storm_obj[sub_vars].to_netcdf(path=join(out_path, file_end),
                                  mode="w",
                                  encoding=enc_dict)
    storm_obj.close()


if __name__ == "__main__":
    main()
