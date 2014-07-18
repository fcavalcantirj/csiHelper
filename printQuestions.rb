require 'nokogiri'
require 'open-uri'

f = File.open(ARGV.first)

doc = Nokogiri::XML(f)

translation = Hash[doc.xpath("//translation").children.map{|n| [n.has_attribute?("id") ? n.attribute("id").text : "", n.children.text.strip]}]

questions = doc.xpath("//select1")

out = File.open(ARGV.last, "w") 

questions.each do |q|
	q.children.each do |l|
		if l.has_attribute? "ref"
			label = l.attribute("ref").text.gsub("jr:itext('","").gsub("')","")
			out << translation[label]+"\n"
		else
			l.children.each do |i|
				if i.has_attribute? "ref"
						label = i.attribute("ref").text.gsub("jr:itext('","").gsub("')","")
						out << "		#{translation[label]}\n"
				else
						out << "		#{i.text.strip}\n"
				end
			end 
		end
	end
end

out.close

f.close()