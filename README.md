# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 453
- HTTP: 139 alive / 83 gold
- HTTPS: 122 alive / 32 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 197 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46835
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
