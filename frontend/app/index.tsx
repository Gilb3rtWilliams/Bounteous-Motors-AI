import { useNavigation } from "@react-navigation/native";
import { StyleSheet, Text, View } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

import PrimaryButton from "../src/components/PrimaryButton";
import { Colors } from "../src/theme/colors";

export default function HomeScreen() {
  const navigation = useNavigation<any>();

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.content}>
        <Text style={styles.logo}>🚘</Text>

        <Text style={styles.title}>Bounteous Motors AI</Text>

        <Text style={styles.subtitle}>AI Vehicle Price Predictor</Text>

        <Text style={styles.description}>
          Get an accurate vehicle price prediction using Machine Learning.
        </Text>

        <PrimaryButton
          title="Start Prediction"
          onPress={() => navigation.navigate("vehicle-details")}
        />

        <Text style={styles.footer}>Powered by Artificial Intelligence</Text>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: Colors.background,
  },

  content: {
    flex: 1,
    justifyContent: "center",
    padding: 24,
  },

  logo: {
    fontSize: 80,
    textAlign: "center",
    marginBottom: 20,
  },

  title: {
    color: Colors.text,
    fontSize: 34,
    fontWeight: "bold",
    textAlign: "center",
  },

  subtitle: {
    color: Colors.primary,
    fontSize: 22,
    textAlign: "center",
    marginTop: 10,
    fontWeight: "600",
  },

  description: {
    color: Colors.textSecondary,
    fontSize: 16,
    textAlign: "center",
    marginTop: 20,
    lineHeight: 24,
    marginBottom: 50,
  },

  footer: {
    color: Colors.textSecondary,
    textAlign: "center",
    marginTop: 40,
  },
});
