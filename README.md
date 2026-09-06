# SyndProxy validated proxy pool

## Current pool

- Alive now: 416
- Gold now: 300
- HTTP: 81 alive / 50 gold
- HTTPS: 40 alive / 7 gold
- SOCKS4: 149 alive / 127 gold
- SOCKS5: 146 alive / 116 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48367
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
