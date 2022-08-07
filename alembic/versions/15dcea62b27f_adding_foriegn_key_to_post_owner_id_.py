"""adding foriegn key to post.owner_id with user.id

Revision ID: 15dcea62b27f
Revises: 985874ad9896
Create Date: 2022-08-07 12:04:11.183785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15dcea62b27f'
down_revision = '985874ad9896'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('posts_user_fk',source_table="posts",referent_table="users",
                          local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('posts_user_fk',table_name="posts")
    op.drop_column('posts','owner_id')
