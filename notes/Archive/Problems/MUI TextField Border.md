---
subtitle: Changing MUI TextField Border Color
---
```tsx
import { Search } from "@mui/icons-material";
import { outlinedInputClasses, styled, TextField } from "@mui/material";

// mui should die https://stackoverflow.com/a/58963947
const StyledTextField = styled(TextField)({
  [`& .${outlinedInputClasses.root} .${outlinedInputClasses.notchedOutline}`]: {
    borderColor: "rgba(0, 0, 0, 0.23) !important", // yes I checked, this important is required
  },
  [`& .${outlinedInputClasses.root}.${outlinedInputClasses.focused} .${outlinedInputClasses.notchedOutline}`]: {
    borderColor: "rgba(0, 0, 0, 0.23) !important",
  },
});

export default function QuickSearch({
  onConfirm,
  searchPlaceholder = "Quick Search",
  text,
  setText,
  isFetching,
}: {
  onConfirm: () => void;
  searchPlaceholder?: string;
  text: string;
  setText: (text: string) => void;
  isFetching?: boolean;
}) {
  return (
    <StyledTextField
      id="outlined-basic"
      variant="outlined"
      className="min-w-[400px]"
      value={text}
      placeholder={searchPlaceholder}
      onKeyDown={(event: any) => {
        if (event.key === "Enter") onConfirm();
      }}
      onChange={(event) => setText(event.target.value)}
    />
  );
}


```