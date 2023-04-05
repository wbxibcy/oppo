BUNDLE_PATH=/home/isimple/magenta/magenta/bundles/attention_rnn.mag
OUTPUT_PATH=/home/isimple/magenta/magenta/music
MID_PATH=/home/isimple/magenta/magenta/models/melody_rnn/emotion_note.mid
CONFIG=attention_rnn

melody_rnn_generate \
--primer_midi=${MID_PATH} \
--config=${CONFIG} \
--bundle_file=${BUNDLE_PATH} \
--output_dir=${OUTPUT_PATH} \
--num_outputs=1 \
--num_steps=160 \