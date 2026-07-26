import * as ImagePicker from "expo-image-picker";
import { router } from "expo-router";
import { useState } from "react";
import { ScrollView, StyleSheet, Text } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

import ImageUploadCard from "../src/components/ImageUploadCard";
import PrimaryButton from "../src/components/PrimaryButton";
import { Colors } from "../src/theme/colors";

export default function UploadImagesScreen() {
  const [frontImage, setFrontImage] = useState<string | null>(null);
  const [interiorImage, setInteriorImage] = useState<string | null>(null);
  const [odometerImage, setOdometerImage] = useState<string | null>(null);

  const pickImage = async (setter: (uri: string | null) => void) => {
    const result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ["images"],
      allowsEditing: true,
      quality: 0.8,
    });

    if (!result.canceled) {
      setter(result.assets[0].uri);
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView
        contentContainerStyle={styles.content}
        showsVerticalScrollIndicator={false}
      >
        <Text style={styles.title}>Vehicle Inspection</Text>

        <Text style={styles.subtitle}>
          Upload a few photos to give our AI additional context about your
          vehicle.
        </Text>

        <ImageUploadCard
          title="Front View"
          icon="car-sport"
          imageUri={frontImage}
          onPress={() => pickImage(setFrontImage)}
        />

        <ImageUploadCard
          title="Interior"
          icon="car"
          imageUri={interiorImage}
          onPress={() => pickImage(setInteriorImage)}
        />

        <ImageUploadCard
          title="Odometer"
          icon="speedometer"
          imageUri={odometerImage}
          onPress={() => pickImage(setOdometerImage)}
        />

        <PrimaryButton
          title="Continue"
          onPress={() => router.push("/processing")}
        />
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: Colors.background,
  },

  content: {
    padding: 24,
    paddingBottom: 40,
  },

  title: {
    color: Colors.text,
    fontSize: 30,
    fontWeight: "700",
    marginBottom: 8,
  },

  subtitle: {
    color: Colors.textSecondary,
    fontSize: 16,
    lineHeight: 24,
    marginBottom: 30,
  },
});
