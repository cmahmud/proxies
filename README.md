# SyndProxy validated proxy pool

## Current pool

- Alive now: 406
- Gold now: 311
- HTTP: 79 alive / 57 gold
- HTTPS: 27 alive / 8 gold
- SOCKS4: 145 alive / 127 gold
- SOCKS5: 155 alive / 119 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48383
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
