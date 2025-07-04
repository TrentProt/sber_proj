"""add topic_id in user_attempts|index

Revision ID: 9e2d7ee565ec
Revises: d054b8ef1807
Create Date: 2025-06-29 20:04:43.859812

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e2d7ee565ec'
down_revision: Union[str, None] = 'd054b8ef1807'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_cases_id'), 'cases', ['id'], unique=False)
    op.drop_constraint('profiles_user_id_key', 'profiles', type_='unique')
    op.create_index(op.f('ix_profiles_id'), 'profiles', ['id'], unique=False)
    op.create_index(op.f('ix_profiles_user_id'), 'profiles', ['user_id'], unique=True)
    op.create_index(op.f('ix_questions_id'), 'questions', ['id'], unique=False)
    op.create_index(op.f('ix_rewards_id'), 'rewards', ['id'], unique=False)
    op.create_index(op.f('ix_section_topic_id'), 'section_topic', ['id'], unique=False)
    op.create_index(op.f('ix_section_topic_topic_id'), 'section_topic', ['topic_id'], unique=False)
    op.create_index(op.f('ix_story_id'), 'story', ['id'], unique=False)
    op.drop_index('ix_tests_title', table_name='tests')
    op.create_index(op.f('ix_tests_id'), 'tests', ['id'], unique=False)
    op.create_index(op.f('ix_tests_type_test'), 'tests', ['type_test'], unique=False)
    op.create_index(op.f('ix_theories_id'), 'theories', ['id'], unique=False)
    op.create_index(op.f('ix_theories_section_topic_id'), 'theories', ['section_topic_id'], unique=False)
    op.create_index(op.f('ix_topics_id'), 'topics', ['id'], unique=False)
    op.add_column('user_attempts', sa.Column('topic_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_user_attempts_count_correct_answer'), 'user_attempts', ['count_correct_answer'], unique=False)
    op.create_index(op.f('ix_user_attempts_score'), 'user_attempts', ['score'], unique=False)
    op.create_index(op.f('ix_user_attempts_topic_id'), 'user_attempts', ['topic_id'], unique=False)
    op.create_foreign_key(None, 'user_attempts', 'topics', ['topic_id'], ['id'])
    op.create_index(op.f('ix_user_reward_reward_id'), 'user_reward', ['reward_id'], unique=False)
    op.create_index(op.f('ix_user_reward_topic_id'), 'user_reward', ['topic_id'], unique=False)
    op.create_index(op.f('ix_user_reward_user_id'), 'user_reward', ['user_id'], unique=False)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_user_reward_user_id'), table_name='user_reward')
    op.drop_index(op.f('ix_user_reward_topic_id'), table_name='user_reward')
    op.drop_index(op.f('ix_user_reward_reward_id'), table_name='user_reward')
    op.drop_constraint(None, 'user_attempts', type_='foreignkey')
    op.drop_index(op.f('ix_user_attempts_topic_id'), table_name='user_attempts')
    op.drop_index(op.f('ix_user_attempts_score'), table_name='user_attempts')
    op.drop_index(op.f('ix_user_attempts_count_correct_answer'), table_name='user_attempts')
    op.drop_column('user_attempts', 'topic_id')
    op.drop_index(op.f('ix_topics_id'), table_name='topics')
    op.drop_index(op.f('ix_theories_section_topic_id'), table_name='theories')
    op.drop_index(op.f('ix_theories_id'), table_name='theories')
    op.drop_index(op.f('ix_tests_type_test'), table_name='tests')
    op.drop_index(op.f('ix_tests_id'), table_name='tests')
    op.create_index('ix_tests_title', 'tests', ['title'], unique=False)
    op.drop_index(op.f('ix_story_id'), table_name='story')
    op.drop_index(op.f('ix_section_topic_topic_id'), table_name='section_topic')
    op.drop_index(op.f('ix_section_topic_id'), table_name='section_topic')
    op.drop_index(op.f('ix_rewards_id'), table_name='rewards')
    op.drop_index(op.f('ix_questions_id'), table_name='questions')
    op.drop_index(op.f('ix_profiles_user_id'), table_name='profiles')
    op.drop_index(op.f('ix_profiles_id'), table_name='profiles')
    op.create_unique_constraint('profiles_user_id_key', 'profiles', ['user_id'])
    op.drop_index(op.f('ix_cases_id'), table_name='cases')
    # ### end Alembic commands ###
