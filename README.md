# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 396
- HTTP: 74 alive / 54 gold
- HTTPS: 44 alive / 14 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36610
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
