# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 214
- HTTP: 136 alive / 33 gold
- HTTPS: 105 alive / 7 gold
- SOCKS4: 177 alive / 83 gold
- SOCKS5: 197 alive / 91 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32783
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
