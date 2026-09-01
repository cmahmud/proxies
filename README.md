# SyndProxy validated proxy pool

## Current pool

- Alive now: 653
- Gold now: 453
- HTTP: 130 alive / 88 gold
- HTTPS: 130 alive / 31 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 213 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46589
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
