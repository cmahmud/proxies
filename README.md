# SyndProxy private pool

## Current pool

- Alive now: 1115
- Gold now: 393
- HTTP: 348 alive / 109 gold
- HTTPS: 255 alive / 31 gold
- SOCKS4: 217 alive / 117 gold
- SOCKS5: 295 alive / 136 gold

## Historical pool

- Discovered: 152741
- Ever alive: 28027
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
