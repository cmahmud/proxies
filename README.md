# SyndProxy private pool

## Current pool

- Alive now: 902
- Gold now: 251
- HTTP: 324 alive / 37 gold
- HTTPS: 195 alive / 8 gold
- SOCKS4: 224 alive / 142 gold
- SOCKS5: 159 alive / 64 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13696
- Ever gold: 429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
