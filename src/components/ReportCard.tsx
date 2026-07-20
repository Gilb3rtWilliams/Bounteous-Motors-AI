import { StyleSheet, Text, View } from "react-native";
import { Colors } from "../theme/colors";

type Props = {
  title: string;
  children: React.ReactNode;
};

export default function ReportCard({ title, children }: Props) {
  return (
    <View style={styles.card}>
      <Text style={styles.title}>{title}</Text>

      {children}
    </View>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: Colors.surface,
    borderRadius: 18,
    borderWidth: 1,
    borderColor: Colors.border,
    padding: 20,
    marginBottom: 20,
  },

  title: {
    color: Colors.primary,
    fontSize: 18,
    fontWeight: "700",
    marginBottom: 15,
  },
});
