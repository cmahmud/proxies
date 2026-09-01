# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 468
- HTTP: 135 alive / 96 gold
- HTTPS: 112 alive / 33 gold
- SOCKS4: 187 alive / 163 gold
- SOCKS5: 198 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46319
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
