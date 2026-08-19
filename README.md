# SyndProxy private pool

## Current pool

- Alive now: 974
- Gold now: 340
- HTTP: 333 alive / 64 gold
- HTTPS: 188 alive / 14 gold
- SOCKS4: 240 alive / 141 gold
- SOCKS5: 213 alive / 121 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15320
- Ever gold: 491

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
