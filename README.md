# SyndProxy private pool

## Current pool

- Alive now: 1062
- Gold now: 492
- HTTP: 368 alive / 157 gold
- HTTPS: 258 alive / 73 gold
- SOCKS4: 220 alive / 141 gold
- SOCKS5: 216 alive / 121 gold

## Historical pool

- Discovered: 119839
- Ever alive: 18367
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
