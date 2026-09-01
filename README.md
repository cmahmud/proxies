# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 425
- HTTP: 103 alive / 70 gold
- HTTPS: 69 alive / 26 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 177 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47045
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
