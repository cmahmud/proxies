# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 425
- HTTP: 109 alive / 81 gold
- HTTPS: 40 alive / 22 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 186 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49470
- Ever gold: 1584

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
