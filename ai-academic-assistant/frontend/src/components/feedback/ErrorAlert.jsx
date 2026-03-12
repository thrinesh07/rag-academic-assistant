export default function ErrorAlert({ message, className = "" }) {
  if (!message) return null;

  return (
    <div className={`alert alert-danger py-2 ${className}`}>
      {message}
    </div>
  );
}