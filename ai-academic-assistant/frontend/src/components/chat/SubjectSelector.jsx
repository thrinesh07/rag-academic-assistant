import { SUBJECTS } from "../../config/constants";

export default function SubjectSelector({ value, onChange }) {
  return (
    <select
      className="form-select w-auto"
      value={value}
      onChange={onChange}
    >
      {SUBJECTS.map((sub) => (
        <option key={sub.value} value={sub.value}>
          {sub.label}
        </option>
      ))}
    </select>
  );
}