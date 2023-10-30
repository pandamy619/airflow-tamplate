<p align="center">
  <a href="" rel="noopener">
 <h3 align="center">Conventional Branch</h3></a>
</p>

## 📝 Table of Contents

- [About](#about)
- [Usage](#usage)
- [Built Using](#built_using)


## 🧐 About <a name = "about"></a>
A consistent branch naming convention is part of code review best practices, and can make life much more easier for anyone who's collaborating and reviewing your code, in addition to using static analysis tools.


## 🎈 Usage <a name="usage"></a>
The branch name should be structured as follows:
```html
<type>/<task_number>/<short_description>

```

### recommendations 

type     | description | 
:------: | :---------- |
docs     |	Updating documentation
feat     |  Adding new functionality
fix      |	Error correction
bug      |	Bug correction
refactor |	Code edits without bug fixes or adding new features

### Example

```bash
docs/LB-0000/update-readme

feat/LB-0000/add-Polish-language

fix/LB-0000/prevent-racing-of-requests
```