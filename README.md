# SyndProxy validated proxy pool

## Current pool

- Alive now: 401
- Gold now: 346
- HTTP: 102 alive / 78 gold
- HTTPS: 41 alive / 22 gold
- SOCKS4: 80 alive / 75 gold
- SOCKS5: 178 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48673
- Ever gold: 1563

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
