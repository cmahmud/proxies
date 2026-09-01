# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 453
- HTTP: 115 alive / 90 gold
- HTTPS: 131 alive / 28 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 227 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46559
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
