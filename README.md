# SyndProxy private pool

## Current pool

- Alive now: 1032
- Gold now: 429
- HTTP: 302 alive / 87 gold
- HTTPS: 224 alive / 19 gold
- SOCKS4: 235 alive / 161 gold
- SOCKS5: 271 alive / 162 gold

## Historical pool

- Discovered: 158238
- Ever alive: 30008
- Ever gold: 1139

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
