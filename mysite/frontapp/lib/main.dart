import 'package:flutter/material.dart';
import 'package:frontapp/models/post.dart';


void main() {
  runApp( MyApp());
}

class QuestionnairePageWidget extends StatelessWidget {
  final QuestionnairePageModel questionnairePage;

  QuestionnairePageWidget({required this.questionnairePage});

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          questionnairePage.sectionTitle,
          style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
        ),
        ...questionnairePage.questions.map((question) {
          return Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                question.questionText,
                style: TextStyle(fontSize: 18),
              ),
              if (question.questionType == 'multiple_choice') ...[
                // Add UI for multiple-choice questions here
              ],
              if (question.questionType == 'text') ...[
                // Add UI for text questions here
              ],
            ],
          );
        }).toList(),
      ],
    );
  }
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text('Questionnaire Page')),
        body: FutureBuilder(
          future: QuestionnaireService().fetchQuestionnairePages(),
          builder: (context, snapshot) {
            if (snapshot.hasError) {
              return Text('Error: ${snapshot.error}');
            } else if (snapshot.hasData) {
              final questionnairePages = snapshot.data as List<QuestionnairePageModel>;
              return ListView.builder(
                itemCount: questionnairePages.length,
                itemBuilder: (context, index) {
                  return QuestionnairePageWidget(questionnairePage: questionnairePages[index]);
                },
              );
            } else {
              return CircularProgressIndicator();
            }
          },
        ),
      ),
    );
  }
}
