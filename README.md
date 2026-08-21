# SyndProxy private pool

## Current pool

- Alive now: 1113
- Gold now: 384
- HTTP: 374 alive / 99 gold
- HTTPS: 280 alive / 28 gold
- SOCKS4: 204 alive / 122 gold
- SOCKS5: 255 alive / 135 gold

## Historical pool

- Discovered: 152221
- Ever alive: 27976
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
