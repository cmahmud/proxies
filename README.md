# SyndProxy private pool

## Current pool

- Alive now: 909
- Gold now: 368
- HTTP: 292 alive / 88 gold
- HTTPS: 203 alive / 17 gold
- SOCKS4: 210 alive / 142 gold
- SOCKS5: 204 alive / 121 gold

## Historical pool

- Discovered: 119839
- Ever alive: 18360
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
