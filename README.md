# extract-code-property-graph

<p>
The <strong>CPG</strong> combines many representations of source code into one queryable graph database. For example, the CPG merges graphs from the compiler such as the <em>Abstract Syntax Tree</em>, the <em>Program Dependence Graph</em>, the <em>Control Flow graph</em>, etc., into a single joint data structure.
</p>

<p>
A property graph is composed of the following building blocks:
</p>

<ol>
<li><strong>Nodes and their types</strong>. Nodes represent program constructs. This includes low-level language constructs such as methods, variables, and control structures, but also higher level constructs such as HTTP endpoints or findings. Each node has a type. The type indicates the type of program construct represented by the node, e.g., a node with the type METHOD represents a method while a node with type LOCAL represents the declaration of a local variable.</li>

<li><strong>Labeled directed edges</strong>. Relations between program constructs are represented via edges between their corresponding nodes. For example, to express that a method contains a local variable, we can create an edge with the label CONTAINS from the method's node to the local's node. By using labeled edges, we can represent multiple types of relations in the same graph. Moreover, edges are directed to express, e.g., that the method contains the local but not the other way around. Multiple edges may exist between the same two nodes.</li>

<li><strong>Key-Value Pairs</strong>. Nodes carry key-value pairs (attributes), where the valid keys depend on the node type. For example, a method has at least a name and a signature while a local declaration has at least the name and the type of the declared variable.</li>
</ol>

<p>
In summary, Code Property Graphs are directed, edge-labeled, attributed multigraphs, and we insist that each node carries at least one attribute that indicates its type.
</p>