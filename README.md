# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 447
- HTTP: 114 alive / 89 gold
- HTTPS: 52 alive / 31 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 175 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49297
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
