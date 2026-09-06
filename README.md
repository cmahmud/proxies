# SyndProxy validated proxy pool

## Current pool

- Alive now: 414
- Gold now: 328
- HTTP: 84 alive / 59 gold
- HTTPS: 36 alive / 14 gold
- SOCKS4: 149 alive / 132 gold
- SOCKS5: 145 alive / 123 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48349
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
