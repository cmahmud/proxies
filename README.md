# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 453
- HTTP: 137 alive / 81 gold
- HTTPS: 130 alive / 35 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 199 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46835
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
