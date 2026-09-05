# SyndProxy validated proxy pool

## Current pool

- Alive now: 394
- Gold now: 312
- HTTP: 106 alive / 77 gold
- HTTPS: 35 alive / 15 gold
- SOCKS4: 83 alive / 73 gold
- SOCKS5: 170 alive / 147 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47834
- Ever gold: 1497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
