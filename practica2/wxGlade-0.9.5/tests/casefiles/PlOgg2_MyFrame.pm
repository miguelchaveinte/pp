# generated by wxGlade "faked test version"
#
# To get wxPerl visit http://www.wxperl.it
#

use Wx qw[:allclasses];
use strict;
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# extra code added using wxGlade
use Time::gmtime;
# end wxGlade

package PlOgg2_MyFrame;

use Wx qw[:everything];
use base qw(Wx::Frame);
use strict;

use Wx::Locale gettext => '_T';
sub new {
    my( $self, $parent, $id, $title, $pos, $size, $style, $name ) = @_;
    $parent = undef              unless defined $parent;
    $id     = -1                 unless defined $id;
    $title  = ""                 unless defined $title;
    $pos    = wxDefaultPosition  unless defined $pos;
    $size   = wxDefaultSize      unless defined $size;
    $name   = ""                 unless defined $name;

    # begin wxGlade: PlOgg2_MyFrame::new
    $style = wxDEFAULT_FRAME_STYLE
        unless defined $style;

    $self = $self->SUPER::new( $parent, $id, $title, $pos, $size, $style, $name );
    $self->SetSize(Wx::Size->new(400, 300));
    $self->{grid_1} = Wx::Grid->new($self, wxID_ANY);
    $self->{static_line_2} = Wx::StaticLine->new($self, wxID_ANY);
    $self->{button_6} = Wx::Button->new($self, wxID_CLOSE, "");

    $self->__set_properties();
    $self->__do_layout();

    # end wxGlade
    return $self;

}


sub __set_properties {
    my $self = shift;
    # begin wxGlade: PlOgg2_MyFrame::__set_properties
    $self->SetTitle(_T("FrameOggCompressionDetails"));
    $self->{grid_1}->CreateGrid(8, 3);
    $self->{button_6}->SetFocus();
    $self->{button_6}->SetDefault();
    # end wxGlade
}

sub __do_layout {
    my $self = shift;
    # begin wxGlade: PlOgg2_MyFrame::__do_layout
    $self->{sizer_5} = Wx::BoxSizer->new(wxVERTICAL);
    $self->{grid_sizer_3} = Wx::FlexGridSizer->new(3, 1, 0, 0);
    $self->{grid_sizer_3}->Add($self->{grid_1}, 1, wxEXPAND, 0);
    $self->{grid_sizer_3}->Add($self->{static_line_2}, 0, wxALL|wxEXPAND, 5);
    $self->{grid_sizer_3}->Add($self->{button_6}, 0, wxALIGN_RIGHT|wxALL, 5);
    $self->{grid_sizer_3}->AddGrowableRow(0);
    $self->{grid_sizer_3}->AddGrowableCol(0);
    $self->{sizer_5}->Add($self->{grid_sizer_3}, 1, wxEXPAND, 0);
    $self->SetSizer($self->{sizer_5});
    $self->Layout();
    # end wxGlade
}

# end of class PlOgg2_MyFrame

1;

