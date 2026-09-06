# SyndProxy validated proxy pool

## Current pool

- Alive now: 412
- Gold now: 315
- HTTP: 83 alive / 51 gold
- HTTPS: 41 alive / 10 gold
- SOCKS4: 143 alive / 135 gold
- SOCKS5: 145 alive / 119 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48367
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
