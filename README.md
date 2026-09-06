# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 353
- HTTP: 123 alive / 74 gold
- HTTPS: 66 alive / 22 gold
- SOCKS4: 139 alive / 113 gold
- SOCKS5: 171 alive / 144 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47985
- Ever gold: 1506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
