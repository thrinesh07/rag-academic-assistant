
export default function Loader({ size = "sm" }) {
  return (
    <div className="text-center py-3">
      <div
        className={`spinner-border text-dark spinner-border-${size}`}
        role="status"
      >
        <span className="visually-hidden">
          Loading...
        </span>
      </div>
    </div>
  );
}