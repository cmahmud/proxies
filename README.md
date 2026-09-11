# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 422
- HTTP: 94 alive / 70 gold
- HTTPS: 57 alive / 25 gold
- SOCKS4: 198 alive / 166 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49078
- Ever gold: 1571

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
