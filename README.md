# SyndProxy private pool

## Current pool

- Alive now: 1088
- Gold now: 446
- HTTP: 357 alive / 102 gold
- HTTPS: 259 alive / 29 gold
- SOCKS4: 210 alive / 151 gold
- SOCKS5: 262 alive / 164 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28748
- Ever gold: 1113

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
