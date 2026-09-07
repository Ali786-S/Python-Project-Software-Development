# Python-Project-Software-Development

## University progression calculator

This project records university credit outcomes and displays a histogram for:

- Progress
- Progress (module trailer)
- Module retriever
- Exclude

### Run it

Use Python 3 from the project directory:

```bash
python w20457325.py
```

Enter pass, defer, and fail credits using values from `0` to `120` in steps of
20. The three values must total 120. Results are saved to `student_data.txt`
when you quit with `q`.

The input validation is also reusable in other programs:

```python
from validation import validate_credits

credits = validate_credits()
print(credits)
```
