import { Ionicons } from "@expo/vector-icons";
import { router } from "expo-router";
import { useEffect, useMemo, useState } from "react";
import { StyleSheet, Text, View } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

import Animated, {
  useAnimatedStyle,
  useSharedValue,
  withRepeat,
  withSequence,
  withTiming,
} from "react-native-reanimated";

import { Colors } from "../src/theme/colors";

const steps = [
  "Vehicle information verified",
  "Historical pricing analyzed",
  "Comparing market prices",
  "Running prediction model",
  "Preparing results",
];

export default function ProcessingScreen() {
  const [progress, setProgress] = useState(0);

  const width = useSharedValue(0);
  const translateY = useSharedValue(0);

  useEffect(() => {
    translateY.value = withRepeat(
      withSequence(
        withTiming(-10, { duration: 800 }),
        withTiming(0, { duration: 800 }),
      ),
      -1,
      true,
    );
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      setProgress((current) => {
        if (current >= 100) {
          clearInterval(interval);

          setTimeout(() => {
            router.replace("/results");
          }, 800);

          return 100;
        }

        return current + 2;
      });
    }, 80);

    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    width.value = withTiming(progress, {
      duration: 100,
    });
  }, [progress]);

  const carAnimation = useAnimatedStyle(() => ({
    transform: [{ translateY: translateY.value }],
  }));

  const progressStyle = useAnimatedStyle(() => ({
    width: `${width.value}%`,
  }));

  const completedSteps = useMemo(() => {
    return Math.floor(progress / 20);
  }, [progress]);

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.content}>
        <Animated.View style={carAnimation}>
          <Ionicons name="car-sport" size={90} color={Colors.primary} />
        </Animated.View>

        <Text style={styles.title}>AI Analysis in Progress</Text>

        <Text style={styles.subtitle}>
          Our machine learning model is analyzing your vehicle and comparing it
          with historical market data.
        </Text>

        <View style={styles.progressContainer}>
          <Animated.View style={[styles.progressBar, progressStyle]} />
        </View>

        <Text style={styles.percent}>{progress}%</Text>

        <View style={styles.stepsContainer}>
          {steps.map((step, index) => {
            const completed = completedSteps > index;

            return (
              <View key={step} style={styles.stepRow}>
                <Ionicons
                  name={completed ? "checkmark-circle" : "ellipse-outline"}
                  size={22}
                  color={completed ? Colors.success : Colors.textSecondary}
                />

                <Text
                  style={[styles.stepText, completed && styles.completedText]}
                >
                  {step}
                </Text>
              </View>
            );
          })}
        </View>

        <Text style={styles.waitText}>Please wait...</Text>
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
    paddingHorizontal: 30,
  },

  title: {
    color: Colors.text,
    fontSize: 28,
    fontWeight: "700",
    textAlign: "center",
    marginTop: 20,
  },

  subtitle: {
    color: Colors.textSecondary,
    textAlign: "center",
    marginTop: 15,
    lineHeight: 24,
    fontSize: 16,
    marginBottom: 35,
  },

  progressContainer: {
    height: 10,
    borderRadius: 50,
    overflow: "hidden",
    backgroundColor: Colors.surface,
  },

  progressBar: {
    height: "100%",
    backgroundColor: Colors.primary,
    borderRadius: 50,
  },

  percent: {
    color: Colors.text,
    fontSize: 22,
    fontWeight: "700",
    marginTop: 12,
    textAlign: "center",
    marginBottom: 35,
  },

  stepsContainer: {
    gap: 18,
  },

  stepRow: {
    flexDirection: "row",
    alignItems: "center",
  },

  stepText: {
    marginLeft: 12,
    color: Colors.textSecondary,
    fontSize: 16,
  },

  completedText: {
    color: Colors.text,
    fontWeight: "600",
  },

  waitText: {
    color: Colors.primary,
    textAlign: "center",
    marginTop: 40,
    fontWeight: "600",
    fontSize: 16,
  },
});
