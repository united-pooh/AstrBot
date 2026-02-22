import { ref } from 'vue';
import axios from 'axios';
import { t } from '@/i18n/composables';

export function useRecording() {
    const isRecording = ref(false);
    const audioChunks = ref<Blob[]>([]);
    const mediaRecorder = ref<MediaRecorder | null>(null);

    async function startRecording(onStart?: (label: string) => void) {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            mediaRecorder.value = new MediaRecorder(stream);
            
            mediaRecorder.value.ondataavailable = (event) => {
                audioChunks.value.push(event.data);
            };
            
            mediaRecorder.value.start();
            isRecording.value = true;
            
            if (onStart) {
                onStart(t('src.composables.userecording.recording_in_progress'));
            }
        } catch (error) {
            console.error('Failed to start recording:', error);
        }
    }

    async function stopRecording(onStop?: (label: string) => void): Promise<string> {
        return new Promise((resolve, reject) => {
            if (!mediaRecorder.value) {
                reject('No media recorder');
                return;
            }

            isRecording.value = false;
            if (onStop) {
                onStop(t('src.composables.userecording.stop_chat_input'));
            }

            mediaRecorder.value.stop();
            mediaRecorder.value.onstop = async () => {
                const audioBlob = new Blob(audioChunks.value, { type: 'audio/wav' });
                audioChunks.value = [];

                mediaRecorder.value?.stream.getTracks().forEach(track => track.stop());

                const formData = new FormData();
                formData.append('file', audioBlob);

                try {
                    const response = await axios.post('/api/chat/post_file', formData, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    });

                    const audio = response.data.data.filename;
                    console.log('Audio uploaded:', audio);
                    resolve(audio);
                } catch (err) {
                    console.error('Error uploading audio:', err);
                    reject(err);
                }
            };
        });
    }

    return {
        isRecording,
        startRecording,
        stopRecording
    };
}

