# global schema Schema

```txt
global.schema.json
```

buildtest global schema is validated for all buildspecs. The global schema defines top-level structure of buildspec and defintions that are inherited for sub-schemas

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                             |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [global.schema.json](../out/global.schema.json "open original schema") |

## global schema Type

`object` ([global schema](global.md))

# global schema Properties

| Property                    | Type      | Required | Nullable       | Defined by                                                                                     |
| :-------------------------- | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------- |
| [skip](#skip)               | `boolean` | Optional | cannot be null | [global schema](definitions-definitions-skip.md "global.schema.json#/properties/skip")         |
| [maintainers](#maintainers) | `array`   | Optional | cannot be null | [global schema](global-properties-maintainers.md "global.schema.json#/properties/maintainers") |
| [buildspecs](#buildspecs)   | `object`  | Required | cannot be null | [global schema](global-properties-buildspecs.md "global.schema.json#/properties/buildspecs")   |

## skip

The `skip` is a boolean field that can be used to skip tests during builds. By default buildtest will build and run all tests in your buildspec file, if `skip: True` is set it will skip the buildspec.

`skip`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [global schema](definitions-definitions-skip.md "global.schema.json#/properties/skip")

### skip Type

`boolean`

## maintainers

One or more maintainers or aliases

`maintainers`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [global schema](global-properties-maintainers.md "global.schema.json#/properties/maintainers")

### maintainers Type

`string[]`

### maintainers Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## buildspecs

This section is used to define one or more tests (buildspecs). Each test must be unique name

`buildspecs`

*   is required

*   Type: `object` ([Details](global-properties-buildspecs.md))

*   cannot be null

*   defined in: [global schema](global-properties-buildspecs.md "global.schema.json#/properties/buildspecs")

### buildspecs Type

`object` ([Details](global-properties-buildspecs.md))
