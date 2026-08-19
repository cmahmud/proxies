# SyndProxy private pool

## Current pool

- Alive now: 1253
- Gold now: 407
- HTTP: 438 alive / 78 gold
- HTTPS: 277 alive / 15 gold
- SOCKS4: 272 alive / 151 gold
- SOCKS5: 266 alive / 163 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20628
- Ever gold: 871

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
