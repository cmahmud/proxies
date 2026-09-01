# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 448
- HTTP: 93 alive / 74 gold
- HTTPS: 107 alive / 32 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 192 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47411
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
