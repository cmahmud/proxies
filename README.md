# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 394
- HTTP: 147 alive / 82 gold
- HTTPS: 54 alive / 24 gold
- SOCKS4: 156 alive / 136 gold
- SOCKS5: 178 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48026
- Ever gold: 1512

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
