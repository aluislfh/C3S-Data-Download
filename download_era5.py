import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels-monthly-means',
    {
        'format': 'grib',
        'product_type': 'monthly_averaged_reanalysis',
        'variable': [
            '10m_u_component_of_wind', '10m_v_component_of_wind', '2m_dewpoint_temperature',
            '2m_temperature', 'mean_sea_level_pressure', 'sea_surface_temperature',
            'surface_net_solar_radiation', 'surface_solar_radiation_downwards', 'top_net_solar_radiation',
            'total_cloud_cover', 'total_precipitation',
        ],
        'year': [
            '2018', '2019', '2020',
            '2022',
        ],
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'time': '00:00',
        'area': [
            26.5, -88.5, 17.5,
            -70.5,
        ],
    },
    'download.grib')
