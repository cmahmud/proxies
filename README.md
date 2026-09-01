# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 458
- HTTP: 138 alive / 86 gold
- HTTPS: 134 alive / 35 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 194 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46825
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
