# SyndProxy validated proxy pool

## Current pool

- Alive now: 433
- Gold now: 333
- HTTP: 84 alive / 61 gold
- HTTPS: 41 alive / 16 gold
- SOCKS4: 157 alive / 135 gold
- SOCKS5: 151 alive / 121 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48351
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
