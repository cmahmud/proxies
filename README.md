# SyndProxy validated proxy pool

## Current pool

- Alive now: 423
- Gold now: 315
- HTTP: 83 alive / 56 gold
- HTTPS: 46 alive / 13 gold
- SOCKS4: 148 alive / 130 gold
- SOCKS5: 146 alive / 116 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48365
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
