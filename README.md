# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 431
- HTTP: 98 alive / 75 gold
- HTTPS: 54 alive / 25 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 181 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49141
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
