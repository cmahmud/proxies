# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 395
- HTTP: 107 alive / 55 gold
- HTTPS: 77 alive / 14 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 203 alive / 166 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33531
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
