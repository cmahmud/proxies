# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 401
- HTTP: 95 alive / 60 gold
- HTTPS: 44 alive / 16 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38981
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
