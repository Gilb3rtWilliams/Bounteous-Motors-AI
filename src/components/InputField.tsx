import { StyleSheet, Text, TextInput, View } from "react-native";
import { Colors } from "../theme/colors";

type Props = {
  label: string;
  value: string;
  onChangeText: (text: string) => void;
  placeholder?: string;
  keyboardType?: "default" | "numeric";
};

export default function InputField({
  label,
  value,
  onChangeText,
  placeholder,
  keyboardType = "default",
}: Props) {
  return (
    <View style={styles.container}>
      <Text style={styles.label}>{label}</Text>

      <TextInput
        value={value}
        onChangeText={onChangeText}
        placeholder={placeholder}
        placeholderTextColor="#777"
        keyboardType={keyboardType}
        style={styles.input}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginBottom: 20,
  },

  label: {
    color: Colors.text,
    marginBottom: 8,
    fontSize: 16,
    fontWeight: "600",
  },

  input: {
    backgroundColor: Colors.surface,
    color: Colors.text,
    borderRadius: 16,
    paddingHorizontal: 18,
    paddingVertical: 16,
    borderWidth: 1,
    borderColor: Colors.border,
    fontSize: 16,
  },
});
