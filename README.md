# SyndProxy validated proxy pool

## Current pool

- Alive now: 361
- Gold now: 187
- HTTP: 115 alive / 39 gold
- HTTPS: 60 alive / 3 gold
- SOCKS4: 71 alive / 63 gold
- SOCKS5: 115 alive / 82 gold

## Historical pool

- Discovered: 169863
- Ever alive: 32716
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
