# SyndProxy validated proxy pool

## Current pool

- Alive now: 387
- Gold now: 303
- HTTP: 103 alive / 75 gold
- HTTPS: 38 alive / 18 gold
- SOCKS4: 78 alive / 68 gold
- SOCKS5: 168 alive / 142 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47848
- Ever gold: 1498

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
