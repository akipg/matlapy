function out = getMdlFilename(mdl)
    info = Simulink.MDLInfo(mdl);
    out = info.Filename;
end