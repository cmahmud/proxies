# SyndProxy private pool

## Current pool

- Alive now: 1859
- Gold now: 615
- HTTP: 801 alive / 236 gold
- HTTPS: 611 alive / 116 gold
- SOCKS4: 187 alive / 103 gold
- SOCKS5: 260 alive / 160 gold

## Historical pool

- Discovered: 143486
- Ever alive: 24790
- Ever gold: 1038

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
