# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 383
- HTTP: 143 alive / 78 gold
- HTTPS: 55 alive / 24 gold
- SOCKS4: 157 alive / 134 gold
- SOCKS5: 180 alive / 147 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48023
- Ever gold: 1511

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
