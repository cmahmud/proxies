# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 449
- HTTP: 113 alive / 82 gold
- HTTPS: 86 alive / 35 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47005
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
