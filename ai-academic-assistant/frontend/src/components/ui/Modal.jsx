export default function Modal({
  id,
  title,
  children,
  footer
}) {
  return (
    <div
      className="modal fade"
      id={id}
      tabIndex="-1"
    >
      <div className="modal-dialog">
        <div className="modal-content">

          <div className="modal-header">
            <h5 className="modal-title">{title}</h5>
            <button
              type="button"
              className="btn-close"
              data-bs-dismiss="modal"
            />
          </div>

          <div className="modal-body">
            {children}
          </div>

          {footer && (
            <div className="modal-footer">
              {footer}
            </div>
          )}

        </div>
      </div>
    </div>
  );
}