# SyndProxy private pool

## Current pool

- Alive now: 869
- Gold now: 319
- HTTP: 263 alive / 35 gold
- HTTPS: 170 alive / 9 gold
- SOCKS4: 222 alive / 142 gold
- SOCKS5: 214 alive / 133 gold

## Historical pool

- Discovered: 103711
- Ever alive: 14022
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
