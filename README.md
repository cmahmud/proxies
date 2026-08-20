# SyndProxy private pool

## Current pool

- Alive now: 773
- Gold now: 376
- HTTP: 206 alive / 75 gold
- HTTPS: 140 alive / 17 gold
- SOCKS4: 211 alive / 144 gold
- SOCKS5: 216 alive / 140 gold

## Historical pool

- Discovered: 148336
- Ever alive: 26305
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
