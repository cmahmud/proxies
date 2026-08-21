# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 392
- HTTP: 346 alive / 101 gold
- HTTPS: 230 alive / 30 gold
- SOCKS4: 194 alive / 121 gold
- SOCKS5: 261 alive / 140 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28064
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
