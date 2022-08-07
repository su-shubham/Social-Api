"""create_post_table

Revision ID: ae57aeaf9378
Revises: 
Create Date: 2022-08-07 11:26:58.271703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae57aeaf9378'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',sa.Column('id',sa.Integer(),primary_key=True,nullable=False),
                    sa.Column('title',sa.String(),nullable=False)
                    )


def downgrade() -> None:
    op.drop_table('posts')
