function out = getMdlOutports(mdl)
    info = Simulink.MDLInfo(mdl);
    out = {info.Interface.Outports.Name};
end