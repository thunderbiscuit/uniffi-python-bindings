# Readme

1. build
2. copy native library in path
3. generate the bindings
4. run the python script

```shell
# build library
cargo build

# copy library in path and rename
cp ./target/debug/libmath.dylib ./src/libuniffi_math.dylib

# generate bindings
uniffi-bindgen generate src/math.udl --language python

# use library
cd ./src/
python3 additions.py
```

## UniFFI
Full [UniFFI docs and user guide here](https://mozilla.github.io/uniffi-rs/Overview.html)  
