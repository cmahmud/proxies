# SyndProxy private pool

## Current pool

- Alive now: 1238
- Gold now: 429
- HTTP: 447 alive / 102 gold
- HTTPS: 269 alive / 26 gold
- SOCKS4: 259 alive / 149 gold
- SOCKS5: 263 alive / 152 gold

## Historical pool

- Discovered: 159282
- Ever alive: 30436
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
