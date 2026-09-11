# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 391
- HTTP: 97 alive / 67 gold
- HTTPS: 39 alive / 21 gold
- SOCKS4: 156 alive / 131 gold
- SOCKS5: 196 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48764
- Ever gold: 1565

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
