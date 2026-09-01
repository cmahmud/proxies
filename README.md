# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 473
- HTTP: 136 alive / 95 gold
- HTTPS: 127 alive / 37 gold
- SOCKS4: 187 alive / 162 gold
- SOCKS5: 195 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46347
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
