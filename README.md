# SyndProxy validated proxy pool

## Current pool

- Alive now: 656
- Gold now: 453
- HTTP: 119 alive / 89 gold
- HTTPS: 131 alive / 29 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 224 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46549
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
