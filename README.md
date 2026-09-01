# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 430
- HTTP: 96 alive / 74 gold
- HTTPS: 65 alive / 28 gold
- SOCKS4: 178 alive / 158 gold
- SOCKS5: 178 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47024
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
