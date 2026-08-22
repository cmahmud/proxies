# SyndProxy private pool

## Current pool

- Alive now: 936
- Gold now: 429
- HTTP: 285 alive / 100 gold
- HTTPS: 229 alive / 32 gold
- SOCKS4: 187 alive / 137 gold
- SOCKS5: 235 alive / 160 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31085
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
