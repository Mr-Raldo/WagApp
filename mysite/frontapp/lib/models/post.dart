import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:http/retry.dart';

class QuestionnaireService {
  final String _baseUrl = 'http://localhost:8000';

  Future<List<QuestionnairePageModel>> fetchQuestionnairePages() async {
    final response = await http.get(Uri.parse('$_baseUrl/api/v2/pages/20/'));

    if (response.statusCode == 200) {
      final jsonBody = json.decode(response.body);
      final questionnairePagesJson = jsonBody['results'] as List<dynamic>;
      final questionnairePages = questionnairePagesJson.map((json) => QuestionnairePageModel.fromJson(json)).toList();
      return questionnairePages;
    } else {
      throw Exception('Failed to load questionnaire pages');
    }
  }
}

class QuestionnairePageModel {
  final int id;
  final String sectionTitle;
  final List<QuestionModel> questions;

  QuestionnairePageModel({
    required this.id,
    required this.sectionTitle,
    required this.questions,
  });

  factory QuestionnairePageModel.fromJson(Map<String, dynamic> json) {
    final questionsJson = json['sections'] as List<dynamic>;
    final questions = questionsJson.map((questionJson) => QuestionModel.fromJson(questionJson)).toList();
    return QuestionnairePageModel(
      id: json['id'],
      sectionTitle: json['section_title'],
      questions: questions,
    );
  }
}

class QuestionModel {
  final String questionText;
  final String questionType;

  QuestionModel({
    required this.questionText,
    required this.questionType,
  });

  factory QuestionModel.fromJson(Map<String, dynamic> json) {
    return QuestionModel(
      questionText: json['question_text'],
      questionType: json['question_type'],
    );
  }
}