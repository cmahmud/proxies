# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 453
- HTTP: 114 alive / 86 gold
- HTTPS: 126 alive / 31 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 193 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46744
- Ever gold: 1448

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
