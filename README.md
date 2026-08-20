# SyndProxy private pool

## Current pool

- Alive now: 749
- Gold now: 384
- HTTP: 215 alive / 74 gold
- HTTPS: 131 alive / 19 gold
- SOCKS4: 208 alive / 150 gold
- SOCKS5: 195 alive / 141 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25615
- Ever gold: 1069

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
