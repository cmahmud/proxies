# SyndProxy private pool

## Current pool

- Alive now: 1215
- Gold now: 412
- HTTP: 426 alive / 82 gold
- HTTPS: 253 alive / 14 gold
- SOCKS4: 271 alive / 157 gold
- SOCKS5: 265 alive / 159 gold

## Historical pool

- Discovered: 131729
- Ever alive: 20796
- Ever gold: 875

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
