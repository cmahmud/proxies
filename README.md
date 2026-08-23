# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 379
- HTTP: 100 alive / 44 gold
- HTTPS: 44 alive / 13 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 213 alive / 162 gold

## Historical pool

- Discovered: 172322
- Ever alive: 32980
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
