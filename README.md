# SyndProxy private pool

## Current pool

- Alive now: 937
- Gold now: 387
- HTTP: 295 alive / 81 gold
- HTTPS: 186 alive / 27 gold
- SOCKS4: 197 alive / 123 gold
- SOCKS5: 259 alive / 156 gold

## Historical pool

- Discovered: 164916
- Ever alive: 32140
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
