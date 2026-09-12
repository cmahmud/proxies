# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 419
- HTTP: 98 alive / 74 gold
- HTTPS: 46 alive / 24 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 188 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49486
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
