# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 412
- HTTP: 114 alive / 69 gold
- HTTPS: 142 alive / 15 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41286
- Ever gold: 1320

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
