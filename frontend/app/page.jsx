export default function Home() {
  return (
    <main
      style={{
        margin: 0,
        padding: 0,
        width: "100%",
        height: "100dvh",
        overflow: "hidden"
      }}
    >
      <iframe
        src="/Chatkie-Web-App/legacy.html"
        title="ChatKie"
        style={{
          width: "100%",
          height: "100%",
          border: "none",
          display: "block"
        }}
      />
    </main>
  );
}
