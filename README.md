# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 426
- HTTP: 98 alive / 69 gold
- HTTPS: 68 alive / 27 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 181 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47043
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
