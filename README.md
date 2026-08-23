# SyndProxy validated proxy pool

## Current pool

- Alive now: 363
- Gold now: 183
- HTTP: 117 alive / 39 gold
- HTTPS: 62 alive / 3 gold
- SOCKS4: 71 alive / 66 gold
- SOCKS5: 113 alive / 75 gold

## Historical pool

- Discovered: 169863
- Ever alive: 32716
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
