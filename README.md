# SyndProxy private pool

## Current pool

- Alive now: 893
- Gold now: 391
- HTTP: 272 alive / 83 gold
- HTTPS: 213 alive / 24 gold
- SOCKS4: 198 alive / 136 gold
- SOCKS5: 210 alive / 148 gold

## Historical pool

- Discovered: 151057
- Ever alive: 27281
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
