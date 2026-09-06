# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 349
- HTTP: 120 alive / 73 gold
- HTTPS: 63 alive / 22 gold
- SOCKS4: 130 alive / 109 gold
- SOCKS5: 172 alive / 145 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47981
- Ever gold: 1506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
