# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 361
- HTTP: 125 alive / 78 gold
- HTTPS: 66 alive / 22 gold
- SOCKS4: 144 alive / 114 gold
- SOCKS5: 175 alive / 147 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47987
- Ever gold: 1506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
