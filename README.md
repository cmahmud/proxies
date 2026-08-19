# SyndProxy private pool

## Current pool

- Alive now: 1209
- Gold now: 471
- HTTP: 425 alive / 121 gold
- HTTPS: 295 alive / 75 gold
- SOCKS4: 241 alive / 141 gold
- SOCKS5: 248 alive / 134 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16517
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
