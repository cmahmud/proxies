# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 377
- HTTP: 107 alive / 43 gold
- HTTPS: 50 alive / 13 gold
- SOCKS4: 188 alive / 159 gold
- SOCKS5: 208 alive / 162 gold

## Historical pool

- Discovered: 172322
- Ever alive: 32980
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
