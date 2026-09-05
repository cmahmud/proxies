# SyndProxy validated proxy pool

## Current pool

- Alive now: 385
- Gold now: 308
- HTTP: 102 alive / 77 gold
- HTTPS: 50 alive / 22 gold
- SOCKS4: 80 alive / 74 gold
- SOCKS5: 153 alive / 135 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47929
- Ever gold: 1505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
