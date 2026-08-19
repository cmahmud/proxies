# SyndProxy private pool

## Current pool

- Alive now: 928
- Gold now: 281
- HTTP: 306 alive / 66 gold
- HTTPS: 235 alive / 18 gold
- SOCKS4: 193 alive / 99 gold
- SOCKS5: 194 alive / 98 gold

## Historical pool

- Discovered: 109961
- Ever alive: 15410
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
