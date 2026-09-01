# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 448
- HTTP: 129 alive / 82 gold
- HTTPS: 126 alive / 32 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 188 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46845
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
