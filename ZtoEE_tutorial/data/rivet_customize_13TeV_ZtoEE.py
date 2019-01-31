import FWCore.ParameterSet.Config as cms

def customise(process):
        process.load('GeneratorInterface.RivetInterface.rivetAnalyzer_cfi')
        process.rivetAnalyzer.AnalysisNames = cms.vstring('MC_ZINC_EL', 'MC_ZJETS_EL', 'ATLAS_2017_I1514251_EL')
	process.rivetAnalyzer.OutputFile = cms.string('sherpa_output.yoda')
	process.rivetAnalyzer.CrossSection = cms.double(1.)
        process.generation_step+=process.rivetAnalyzer
	process.rivetAnalyzer.UseExternalWeight = cms.bool(True)
return(process)
