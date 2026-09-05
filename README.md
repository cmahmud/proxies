# SyndProxy validated proxy pool

## Current pool

- Alive now: 388
- Gold now: 308
- HTTP: 103 alive / 77 gold
- HTTPS: 35 alive / 18 gold
- SOCKS4: 77 alive / 69 gold
- SOCKS5: 173 alive / 144 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47838
- Ever gold: 1498

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
