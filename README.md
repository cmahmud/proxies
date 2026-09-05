# SyndProxy validated proxy pool

## Current pool

- Alive now: 389
- Gold now: 308
- HTTP: 103 alive / 77 gold
- HTTPS: 37 alive / 18 gold
- SOCKS4: 75 alive / 70 gold
- SOCKS5: 174 alive / 143 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47837
- Ever gold: 1498

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
