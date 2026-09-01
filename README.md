# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 453
- HTTP: 125 alive / 88 gold
- HTTPS: 124 alive / 31 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 213 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46591
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
