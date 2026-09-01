# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 425
- HTTP: 92 alive / 71 gold
- HTTPS: 54 alive / 26 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47028
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
