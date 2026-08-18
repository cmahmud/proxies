# SyndProxy private pool

## Current pool

- Alive now: 845
- Gold now: 284
- HTTP: 248 alive / 26 gold
- HTTPS: 140 alive / 5 gold
- SOCKS4: 240 alive / 144 gold
- SOCKS5: 217 alive / 109 gold

## Historical pool

- Discovered: 99957
- Ever alive: 12363
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
