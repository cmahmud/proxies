# SyndProxy private pool

## Current pool

- Alive now: 743
- Gold now: 380
- HTTP: 200 alive / 74 gold
- HTTPS: 127 alive / 20 gold
- SOCKS4: 209 alive / 148 gold
- SOCKS5: 207 alive / 138 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25615
- Ever gold: 1069

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
