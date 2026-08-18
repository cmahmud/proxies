# SyndProxy private pool

## Current pool

- Alive now: 1066
- Gold now: 348
- HTTP: 387 alive / 49 gold
- HTTPS: 216 alive / 14 gold
- SOCKS4: 235 alive / 145 gold
- SOCKS5: 228 alive / 140 gold

## Historical pool

- Discovered: 107115
- Ever alive: 14855
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
