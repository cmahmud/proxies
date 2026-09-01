# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 459
- HTTP: 140 alive / 89 gold
- HTTPS: 138 alive / 32 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 186 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46657
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
