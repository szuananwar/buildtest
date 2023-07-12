# Untitled array in spack schema version Schema

```txt
spack.schema.json#/properties/sbatch
```

This field is used for specifying #SBATCH options in test script.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                             |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [spack.schema.json\*](../out/spack.schema.json "open original schema") |

## sbatch Type

`string[]`

## sbatch Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
