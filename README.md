# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 445
- HTTP: 134 alive / 78 gold
- HTTPS: 118 alive / 30 gold
- SOCKS4: 188 alive / 165 gold
- SOCKS5: 191 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47639
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
