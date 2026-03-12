export default function Select({
  label,
  options = [],
  value,
  onChange,
  className = ""
}) {
  return (
    <div className="mb-3">
      {label && <label className="form-label">{label}</label>}

      <select
        className={`form-select ${className}`}
        value={value}
        onChange={onChange}
      >
        {options.map((opt) => (
          <option key={opt.value} value={opt.value}>
            {opt.label}
          </option>
        ))}
      </select>
    </div>
  );
}