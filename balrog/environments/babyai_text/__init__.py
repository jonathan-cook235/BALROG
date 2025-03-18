from .clean_lang_wrapper import BabyAITextCleanLangWrapper

PLAN_INSTRUCTION = """
Instead of a normal action, you have the option to make a high-level plan for completing the task. 
Your plan should include reasoning about how to solve the task.
Output your plan strictly in the following format:

<plan>YOUR_PLAN</plan>

Replace YOUR_PLAN with your own thinking and plan. Output no other text.
""".strip()

ACTIONS = {
    "turn left": "turn to the left",
    "turn right": "turn to the right",
    "go forward": "take one step forward",
    "pick up": "pick up the object below you",
    "drop": "drop the object that you are holding",
    "toggle": "manipulate the object in front of you",
    "<plan>": PLAN_INSTRUCTION
}


def get_instruction_prompt(env, mission="BabyAI-MixedTrainLocal-v0"):
    action_strings = ",\n".join(f"{action}: {description}" for action, description in ACTIONS.items())

    instruction_prompt = f"""
You are an agent playing a simple navigation game. Your goal is to {mission}. The following are the possible actions you can take in the game, followed by a short description of each action:

{action_strings}.

In a moment I will present you an observation.

Tips:
- Once the desired object you want to interact or pickup in front of you, you can use the 'toggle' action to interact with it.
- It doesn't make sense to repeat the same action over and over if the observation doesn't change.

PLAY!
""".strip()

    return instruction_prompt
