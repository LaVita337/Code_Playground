import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:tiktok_practice/constants/gaps.dart';
import 'package:tiktok_practice/constants/sizes.dart';
import 'package:tiktok_practice/features/authentication/login_screen.dart';
import 'package:tiktok_practice/features/authentication/username_screen.dart';
import 'package:tiktok_practice/features/authentication/widgets/auth_button.dart';

class SignUpScreen extends StatelessWidget {
  const SignUpScreen({super.key});

  void _onLoginTap(BuildContext context) {
    Navigator.of(context).pop(
      MaterialPageRoute(
        builder: (context) => const LoginScreen(),
      ),
    );
  }

  void _onEmailSignUpTap(BuildContext context) {
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (context) => const UsernameScreen(),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: Sizes.size40),
          child: Column(
            children: [
              Gaps.v80,
              const Text(
                'Sign up for TikTok',
                style: TextStyle(
                  fontSize: Sizes.size24,
                  fontWeight: FontWeight.w700,
                ),
              ),
              Gaps.v20,
              const Text(
                'Create a profile, follow other accounts, make your own videos, and more.',
                style: TextStyle(
                  fontSize: Sizes.size16,
                  color: Colors.black54,
                ),
                textAlign: TextAlign.center,
              ),
              Gaps.v40,
              AuthButton(
                  onTapFunction: _onEmailSignUpTap,
                  icon: const FaIcon(FontAwesomeIcons.user),
                  text: 'Use Email & Password'),
              Gaps.v16,
              AuthButton(
                  onTapFunction: _onEmailSignUpTap,
                  icon: const FaIcon(FontAwesomeIcons.facebook),
                  text: 'Continue with Facebook'),
              Gaps.v16,
              AuthButton(
                  onTapFunction: _onEmailSignUpTap,
                  icon: const FaIcon(FontAwesomeIcons.apple),
                  text: 'Continue with Apple'),
              Gaps.v16,
              AuthButton(
                  onTapFunction: _onEmailSignUpTap,
                  icon: const FaIcon(FontAwesomeIcons.google),
                  text: 'Continue with Google'),
              Gaps.v16,
            ],
          ),
        ),
      ),
      bottomNavigationBar: BottomAppBar(
        elevation: 2,
        color: Colors.grey.shade50,
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: Sizes.size32),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Text(
                'Already have an account?',
                style: TextStyle(
                  fontSize: Sizes.size14,
                  fontWeight: FontWeight.w400,
                ),
              ),
              Gaps.h5,
              GestureDetector(
                onTap: () => _onLoginTap(context),
                child: Text(
                  'Log in',
                  style: TextStyle(
                      color: Theme.of(context).primaryColor,
                      fontSize: Sizes.size16,
                      fontWeight: FontWeight.w600),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
