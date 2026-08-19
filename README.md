# SyndProxy private pool

## Current pool

- Alive now: 1145
- Gold now: 539
- HTTP: 408 alive / 164 gold
- HTTPS: 285 alive / 90 gold
- SOCKS4: 219 alive / 140 gold
- SOCKS5: 233 alive / 145 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18633
- Ever gold: 722

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
