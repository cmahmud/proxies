# SyndProxy private pool

## Current pool

- Alive now: 724
- Gold now: 376
- HTTP: 167 alive / 74 gold
- HTTPS: 138 alive / 18 gold
- SOCKS4: 226 alive / 149 gold
- SOCKS5: 193 alive / 135 gold

## Historical pool

- Discovered: 148336
- Ever alive: 26251
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
