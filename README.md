# SyndProxy validated proxy pool

## Current pool

- Alive now: 414
- Gold now: 304
- HTTP: 81 alive / 51 gold
- HTTPS: 41 alive / 9 gold
- SOCKS4: 147 alive / 129 gold
- SOCKS5: 145 alive / 115 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48367
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
