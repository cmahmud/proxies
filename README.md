# SyndProxy private pool

## Current pool

- Alive now: 1078
- Gold now: 480
- HTTP: 391 alive / 130 gold
- HTTPS: 263 alive / 78 gold
- SOCKS4: 210 alive / 121 gold
- SOCKS5: 214 alive / 151 gold

## Historical pool

- Discovered: 119696
- Ever alive: 17875
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
