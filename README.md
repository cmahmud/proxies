# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 357
- HTTP: 127 alive / 77 gold
- HTTPS: 64 alive / 22 gold
- SOCKS4: 142 alive / 113 gold
- SOCKS5: 174 alive / 145 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47987
- Ever gold: 1506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
