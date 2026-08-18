# SyndProxy private pool

## Current pool

- Alive now: 964
- Gold now: 341
- HTTP: 336 alive / 65 gold
- HTTPS: 180 alive / 14 gold
- SOCKS4: 235 alive / 141 gold
- SOCKS5: 213 alive / 121 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15320
- Ever gold: 491

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
