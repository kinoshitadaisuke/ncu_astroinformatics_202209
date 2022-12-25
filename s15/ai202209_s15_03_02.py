#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/25 20:32:35 (CST) daisuke>
#

# data files (distance table and velocity table)
file_d = 'lvg_d.data'
file_v = 'lvg_v.data'

# output file name
file_output = 'lvg.data'

# dictionary to store data
data_d = {}
data_v = {}

# opening file
with open (file_d, 'r') as fh_d:
    # reading distance table
    counter = 0
    for line in fh_d:
        # increment the counter if the line starts with '-'.
        if (line[0] == '-'):
            counter += 1
        # stop processing the line if the counter is smaller than 4.
        if ( (counter < 4) or (line[0] == '-') ):
            continue
        # extracting data
        name_str     = line[0:18].strip ()
        dm_str       = line[19:24].strip ()
        dm_err_str   = line[25:29].strip ()
        d_method_str = line[30:34].strip ()
        # conversion from string to float
        dm = float (dm_str)
        if (dm_err_str == ''):
            dm_err = 0.0
        else:
            dm_err = float (dm_err_str)
        # calculation of distance in Mpc
        dist_pc      = 10**(dm / 5.0 + 1.0)
        dist_Mpc     = dist_pc * 10**-6
        dist_pc_err  = 10**( (dm + dm_err) / 5.0 + 1.0 ) - dist_pc
        dist_Mpc_err = dist_pc_err * 10**-6
        # constructing dictionary
        data_d[name_str]                 = {}
        data_d[name_str]['dm']           = dm
        data_d[name_str]['dm_err']       = dm_err
        data_d[name_str]['dist_Mpc']     = dist_Mpc
        data_d[name_str]['dist_Mpc_err'] = dist_Mpc_err
        data_d[name_str]['method']       = d_method_str

# opening file
with open (file_v, 'r') as fh_v:
    # reading velocity table
    counter = 0
    for line in fh_v:
        # increment the counter if the line starts with '-'.
        if (line[0] == '-'):
            counter += 1
        # stop processing the line if the counter is smaller than 4.
        if ( (counter < 3) or (line[0] == '-') ):
            continue
        # extracting data
        name_str    = line[0:18].strip ()
        vel_str     = line[19:23].strip ()
        vel_err_str = line[24:27].strip ()
        # conversion from string to float
        vel = float (vel_str)
        if (vel_err_str == ''):
            vel_err = 0.0
        else:
            vel_err = float (vel_err_str)
        # constructing dictionary
        data_v[name_str] = {}
        data_v[name_str]['vel'] = vel
        data_v[name_str]['vel_err'] = vel_err

with open (file_output, 'w') as fh_out:
    # printing the header
    header = f"# LVG galaxies with known distance and velocity\n" \
        + f"# distance in Mpc, distance error in Mpc,\n" \
        + f"# velocity in km/s, velocity error in km/s,\n" \
        + f"# method of distance determination, name of galaxy\n"
    fh_out.write (header)

    # finding galaxies with both known distance and velocity
    # sorting the data by distance
    for name in sorted (data_d, key=lambda x: data_d[x]['dist_Mpc']):
        # if a galaxy has velocity data, then we print the data.
        if name in data_v:
            # printing data
            record = f"{data_d[name]['dist_Mpc']:12.6f}" \
                + f" {data_d[name]['dist_Mpc_err']:12.6f}" \
                + f" {data_v[name]['vel']:12.6f}" \
                + f" {data_v[name]['vel_err']:12.6f}" \
                + f" # {data_d[name]['method']}, {name}\n"
            fh_out.write (record)
