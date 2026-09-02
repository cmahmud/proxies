# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 441
- HTTP: 97 alive / 70 gold
- HTTPS: 110 alive / 32 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 182 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47447
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
