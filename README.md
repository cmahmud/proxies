# SyndProxy private pool

## Current pool

- Alive now: 1243
- Gold now: 568
- HTTP: 466 alive / 192 gold
- HTTPS: 344 alive / 94 gold
- SOCKS4: 213 alive / 148 gold
- SOCKS5: 220 alive / 134 gold

## Historical pool

- Discovered: 138338
- Ever alive: 22939
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
