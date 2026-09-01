# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 446
- HTTP: 124 alive / 85 gold
- HTTPS: 130 alive / 30 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 215 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46606
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
