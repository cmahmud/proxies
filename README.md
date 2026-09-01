# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 459
- HTTP: 146 alive / 90 gold
- HTTPS: 116 alive / 35 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 198 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46874
- Ever gold: 1453

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
