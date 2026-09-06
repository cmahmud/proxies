# SyndProxy validated proxy pool

## Current pool

- Alive now: 410
- Gold now: 327
- HTTP: 82 alive / 59 gold
- HTTPS: 34 alive / 14 gold
- SOCKS4: 151 alive / 134 gold
- SOCKS5: 143 alive / 120 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48349
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
