# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 450
- HTTP: 124 alive / 85 gold
- HTTPS: 124 alive / 31 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 214 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46596
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
