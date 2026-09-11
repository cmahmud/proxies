# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 438
- HTTP: 109 alive / 75 gold
- HTTPS: 60 alive / 27 gold
- SOCKS4: 196 alive / 170 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49098
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
