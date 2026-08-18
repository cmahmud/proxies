# SyndProxy private pool

## Current pool

- Alive now: 1013
- Gold now: 237
- HTTP: 364 alive / 30 gold
- HTTPS: 161 alive / 8 gold
- SOCKS4: 274 alive / 113 gold
- SOCKS5: 214 alive / 86 gold

## Historical pool

- Discovered: 86712
- Ever alive: 6858
- Ever gold: 316

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
