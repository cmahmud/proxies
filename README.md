# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 448
- HTTP: 124 alive / 86 gold
- HTTPS: 133 alive / 31 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 215 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46607
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
