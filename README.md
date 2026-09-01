# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 461
- HTTP: 137 alive / 92 gold
- HTTPS: 134 alive / 34 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 189 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46683
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
