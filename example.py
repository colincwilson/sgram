from sgram import sgram

sfile = 'short_mono_example.wav'
(f, ts, S) = sgram( \
    sfile,
    tf=5000,
    band='nb',
    save_name='example_nb.png',
    cmap='Spectral_r')

print(f.shape)
print(ts.shape)
print(S.shape)
