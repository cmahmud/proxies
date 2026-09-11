# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 359
- HTTP: 90 alive / 75 gold
- HTTPS: 61 alive / 32 gold
- SOCKS4: 165 alive / 75 gold
- SOCKS5: 208 alive / 177 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48585
- Ever gold: 1556

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
