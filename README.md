# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 394
- HTTP: 84 alive / 64 gold
- HTTPS: 86 alive / 17 gold
- SOCKS4: 160 alive / 153 gold
- SOCKS5: 167 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43335
- Ever gold: 1369

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
