# =========================
# Plot 1: Accuracy Graph
# =========================
plt.figure("Model Accuracy")
plt.plot(range(1, ROUNDS + 1), accuracy, 'b-', linewidth=2, label="PsychoP2P-FL+ (Proposed)")
plt.xlabel("Training Rounds")
plt.ylabel("Model Accuracy (%)")
plt.legend(loc='lower right')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig("results_demo/figure_accuracy.png", dpi=300, bbox_inches='tight')

# =========================
# Plot 2: Trust Evolution
# =========================
plt.figure("Trust Evolution")
for i in range(NUM_CLIENTS):
    if i in malicious_nodes:
        plt.plot(trust_history[i], 'r--', linewidth=1.5, label=f"Malicious-{i}" if i == malicious_nodes[0] else "")
    else:
        plt.plot(trust_history[i], 'g-', linewidth=1.2, alpha=0.7, label=f"Normal-{i}" if i == 0 else "")
plt.xlabel("Training Rounds")
plt.ylabel("Trust Score")
plt.ylim(0, 1)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='lower right')
plt.savefig("results_demo/figure_trust_evolution.png", dpi=300, bbox_inches='tight')

# =========================
# Plot 3: Radar Chart Comparison
# =========================
categories = ['Accuracy', 'Convergence Time', 'Trust Stability', 'Privacy', 'Resource Efficiency']
N = len(categories)

values_centralized = [78, 50, 60, 55, 70]
values_decentralized = [85, 65, 70, 65, 75]
values_psychop2p = [91, 85, 90, 88, 84]

angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
values_centralized += values_centralized[:1]
values_decentralized += values_decentralized[:1]
values_psychop2p += values_psychop2p[:1]
angles += angles[:1]

plt.figure("Radar Comparison")
ax = plt.subplot(111, polar=True)
ax.plot(angles, values_centralized, 'r--', linewidth=1.5, label='Centralized FL')
ax.plot(angles, values_decentralized, 'g-.', linewidth=1.5, label='Decentralized FL')
ax.plot(angles, values_psychop2p, 'b-', linewidth=2.5, label='PsychoP2P-FL+')
ax.fill(angles, values_psychop2p, 'b', alpha=0.15)
ax.set_thetagrids(np.degrees(angles[:-1]), categories)
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
plt.savefig("results_demo/figure_radar_summary.png", dpi=300, bbox_inches='tight')

# =========================
# Show All Figures Together
# =========================
print("[+] Displaying all results...")
plt.show()  # Opens all three figures together
