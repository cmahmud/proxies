# SyndProxy private pool

## Current pool

- Alive now: 1215
- Gold now: 463
- HTTP: 452 alive / 125 gold
- HTTPS: 287 alive / 75 gold
- SOCKS4: 220 alive / 118 gold
- SOCKS5: 256 alive / 145 gold

## Historical pool

- Discovered: 117109
- Ever alive: 17256
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
