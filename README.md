# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 383
- HTTP: 83 alive / 55 gold
- HTTPS: 51 alive / 13 gold
- SOCKS4: 162 alive / 155 gold
- SOCKS5: 177 alive / 160 gold

## Historical pool

- Discovered: 175243
- Ever alive: 33121
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
