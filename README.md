# SyndProxy private pool

## Current pool

- Alive now: 1050
- Gold now: 402
- HTTP: 344 alive / 107 gold
- HTTPS: 266 alive / 21 gold
- SOCKS4: 216 alive / 149 gold
- SOCKS5: 224 alive / 125 gold

## Historical pool

- Discovered: 153722
- Ever alive: 28532
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
