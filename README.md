# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 386
- HTTP: 156 alive / 81 gold
- HTTPS: 59 alive / 23 gold
- SOCKS4: 160 alive / 131 gold
- SOCKS5: 185 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48011
- Ever gold: 1509

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
