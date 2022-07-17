function out = getMdlInports(mdl)
    info = Simulink.MDLInfo(mdl);
    out = {info.Interface.Inports.Name};
end