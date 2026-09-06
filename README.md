# SyndProxy validated proxy pool

## Current pool

- Alive now: 411
- Gold now: 328
- HTTP: 83 alive / 57 gold
- HTTPS: 34 alive / 15 gold
- SOCKS4: 150 alive / 135 gold
- SOCKS5: 144 alive / 121 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48349
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
