# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 449
- HTTP: 125 alive / 85 gold
- HTTPS: 119 alive / 30 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 213 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46598
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
