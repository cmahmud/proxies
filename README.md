# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 395
- HTTP: 106 alive / 56 gold
- HTTPS: 77 alive / 14 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 202 alive / 165 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33531
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
