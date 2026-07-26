import { Ionicons } from "@expo/vector-icons";
import { Image, Pressable, StyleSheet, Text, View } from "react-native";

import { Colors } from "../theme/colors";

type Props = {
  title: string;
  icon: keyof typeof Ionicons.glyphMap;
  imageUri?: string | null;
  onPress: () => void;
};

export default function ImageUploadCard({
  title,
  icon,
  imageUri,
  onPress,
}: Props) {
  return (
    <Pressable style={styles.card} onPress={onPress}>
      <View style={styles.header}>
        <Ionicons name={icon} size={22} color={Colors.primary} />

        <Text style={styles.title}>{title}</Text>
      </View>

      {imageUri ? (
        <>
          <Image source={{ uri: imageUri }} style={styles.image} />

          <View style={styles.successRow}>
            <Ionicons
              name="checkmark-circle"
              size={18}
              color={Colors.success}
            />

            <Text style={styles.successText}>Image Selected</Text>
          </View>
        </>
      ) : (
        <View style={styles.placeholder}>
          <Ionicons
            name="cloud-upload-outline"
            size={40}
            color={Colors.textSecondary}
          />

          <Text style={styles.placeholderText}>Tap to upload</Text>
        </View>
      )}
    </Pressable>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: Colors.surface,
    borderRadius: 18,
    borderWidth: 1,
    borderColor: Colors.border,
    padding: 18,
    marginBottom: 20,
  },

  header: {
    flexDirection: "row",
    alignItems: "center",
    marginBottom: 15,
  },

  title: {
    color: Colors.text,
    fontSize: 17,
    fontWeight: "600",
    marginLeft: 10,
  },

  placeholder: {
    height: 170,
    borderWidth: 2,
    borderColor: Colors.border,
    borderStyle: "dashed",
    borderRadius: 16,
    justifyContent: "center",
    alignItems: "center",
  },

  placeholderText: {
    color: Colors.textSecondary,
    marginTop: 10,
    fontSize: 15,
  },

  image: {
    width: "100%",
    height: 170,
    borderRadius: 14,
  },

  successRow: {
    flexDirection: "row",
    alignItems: "center",
    marginTop: 12,
  },

  successText: {
    color: Colors.success,
    marginLeft: 8,
    fontWeight: "600",
  },
});
