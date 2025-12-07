import os
from audio_separator.separator import Separator

def separate_audio(input_dir: str = '/input', output_dir: str = '/artifacts', model_file: str = 'htdemucs_6s.yaml') -> None:
    os.makedirs(output_dir, exist_ok=True)
    print(f"Output directory: '{output_dir}'")

    if not os.path.exists(input_dir):
        print(f"Input directory '{input_dir}' not found.")
        return

    audio_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.wav', '.mp3', '.flac', '.m4a'))]
    file_count = len(audio_files)

    if file_count == 0:
        print(f"No audio files found in '{input_dir}'.")
        return

    print(f"Found {file_count} file{'s' if file_count != 1 else ''}. Starting separation with model: {model_file}")

    separator = Separator(output_dir=output_dir)
    separator.load_model(model_filename=model_file)

    processed_count = 0
    for file_name in audio_files:
        input_path = os.path.join(input_dir, file_name)
        track_name = os.path.splitext(file_name)[0]
        track_output_dir = os.path.join(output_dir, track_name)
        os.makedirs(track_output_dir, exist_ok=True)

        print(f"Processing {file_name} -> {track_output_dir}")

        try:
            separator.separate(input_path, output_dir=track_output_dir)[1]
            print(f" -> Finished. Stems saved in: {track_output_dir}")
            processed_count += 1
        except Exception as e:
            print(f" -> Error processing {file_name}: {e}")

    print(f"Processed {processed_count}/{file_count} files.")
    print("All files processed successfully." if processed_count == file_count else "Some files failed to process.")

if __name__ == "__main__":
    separate_audio()
