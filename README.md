# SyndProxy private pool

## Current pool

- Alive now: 1091
- Gold now: 554
- HTTP: 416 alive / 186 gold
- HTTPS: 281 alive / 112 gold
- SOCKS4: 193 alive / 118 gold
- SOCKS5: 201 alive / 138 gold

## Historical pool

- Discovered: 124841
- Ever alive: 19303
- Ever gold: 771

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
