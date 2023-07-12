# Untitled string in buildtest configuration schema Schema

```txt
settings.schema.json#/definitions/system/properties/compilers/properties/prgenv_modules/properties/nvhpc
```

Specify name of Programming Environment module for nvhpc

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [settings.schema.json\*](../out/settings.schema.json "open original schema") |

## nvhpc Type

`string`

## nvhpc Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value             | Explanation |
| :---------------- | :---------- |
| `"PrgEnv-nvhpc"`  |             |
| `"PrgEnv-nvidia"` |             |
