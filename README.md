# SyndProxy validated proxy pool

## Current pool

- Alive now: 593
- Gold now: 453
- HTTP: 127 alive / 82 gold
- HTTPS: 103 alive / 36 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 188 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46993
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
