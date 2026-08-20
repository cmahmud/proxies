# SyndProxy private pool

## Current pool

- Alive now: 1582
- Gold now: 652
- HTTP: 543 alive / 218 gold
- HTTPS: 460 alive / 116 gold
- SOCKS4: 239 alive / 159 gold
- SOCKS5: 340 alive / 159 gold

## Historical pool

- Discovered: 141248
- Ever alive: 24146
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
