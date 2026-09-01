# SyndProxy validated proxy pool

## Current pool

- Alive now: 668
- Gold now: 455
- HTTP: 133 alive / 89 gold
- HTTPS: 138 alive / 31 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 215 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46581
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
