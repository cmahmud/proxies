# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 445
- HTTP: 98 alive / 81 gold
- HTTPS: 53 alive / 28 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 184 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49200
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
