import pymiere

def main():
    # Conectar ao Adobe Premiere Pro
    projeto = pymiere.objects.app.project
    sequencia = projeto.activeSequence

    transicoes = ["AI", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "CENTER IN", "CENTER OUT"]
    pasta_transicoes = "Transitions"

    video_tracks = [track for track in sequencia.videoTracks if track.clips.numItems > 0]
    if not video_tracks:
        print("Nenhuma faixa de vídeo com clipes encontrada.")
        return

    target_track_index = video_tracks[0].index + 1

    for i, clip in enumerate(video_tracks[0].clips[:-1]):
        transicao_index = i % len(transicoes)
        transicao_nome = transicoes[transicao_index]
        transicao_caminho = f"{pasta_transicoes}/{transicao_nome}"
        apply_transition(clip, transicao_caminho, target_track_index)

def apply_transition(clip, transition_path, track_index):
    # Função fictícia para aplicar a transição
    print(f"Aplicando transição {transition_path} no clipe {clip.name} na faixa {track_index}")

if __name__ == "__main__":
    main()
