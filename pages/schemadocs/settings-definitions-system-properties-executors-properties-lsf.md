# Untitled object in buildtest configuration schema Schema

```txt
settings.schema.json#/definitions/system/properties/executors/properties/lsf
```

The `lsf` section is used for declaring LSF executors for running jobs using LSF scheduler

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [settings.schema.json\*](../out/settings.schema.json "open original schema") |

## lsf Type

`object` ([Details](settings-definitions-system-properties-executors-properties-lsf.md))

# lsf Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                        |
| :-------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Additional Properties | `object` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-lsf.md "settings.schema.json#/definitions/system/properties/executors/properties/lsf/additionalProperties") |

## Additional Properties

Additional properties are allowed, as long as they follow this schema:

An instance object of lsf executor

*   is optional

*   Type: `object` ([Details](settings-definitions-lsf.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-lsf.md "settings.schema.json#/definitions/system/properties/executors/properties/lsf/additionalProperties")

### additionalProperties Type

`object` ([Details](settings-definitions-lsf.md))
