import { Ionicons } from "@expo/vector-icons";
import { Picker } from "@react-native-picker/picker";
import React from "react";
import {
  StyleSheet,
  Text,
  TextInput,
  TextInputProps,
  View,
} from "react-native";

import { Colors } from "../theme/colors";

type PickerItem = {
  label: string;
  value: string;
};

type FormFieldProps = {
  label: string;
  icon: keyof typeof Ionicons.glyphMap;

  type?: "text" | "picker";

  value: string;

  placeholder?: string;

  keyboardType?: TextInputProps["keyboardType"];

  onChangeText?: (text: string) => void;

  onValueChange?: (value: string) => void;

  items?: PickerItem[];
};

export default function FormField({
  label,
  icon,
  type = "text",
  value,
  placeholder,
  keyboardType = "default",
  onChangeText,
  onValueChange,
  items = [],
}: FormFieldProps) {
  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Ionicons name={icon} size={20} color={Colors.primary} />

        <Text style={styles.label}>{label}</Text>
      </View>

      {type === "text" ? (
        <TextInput
          value={value}
          placeholder={placeholder}
          placeholderTextColor="#777"
          keyboardType={keyboardType}
          onChangeText={onChangeText}
          style={styles.input}
        />
      ) : (
        <View style={styles.pickerContainer}>
          <Picker
            selectedValue={value}
            onValueChange={(itemValue) => onValueChange?.(String(itemValue))}
            dropdownIconColor={Colors.text}
            style={styles.picker}
          >
            {items.map((item) => (
              <Picker.Item
                key={item.value}
                label={item.label}
                value={item.value}
              />
            ))}
          </Picker>
        </View>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginBottom: 18,
  },

  header: {
    flexDirection: "row",
    alignItems: "center",
    marginBottom: 8,
  },

  label: {
    color: Colors.text,
    fontSize: 15,
    fontWeight: "600",
    marginLeft: 8,
  },

  input: {
    backgroundColor: Colors.surface,
    borderRadius: 16,
    borderWidth: 1,
    borderColor: Colors.border,
    color: Colors.text,
    paddingHorizontal: 18,
    paddingVertical: 16,
    fontSize: 16,
  },

  pickerContainer: {
    backgroundColor: Colors.surface,
    borderRadius: 16,
    borderWidth: 1,
    borderColor: Colors.border,
    overflow: "hidden",
  },

  picker: {
    color: Colors.text,
  },
});
