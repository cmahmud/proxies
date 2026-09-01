# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 447
- HTTP: 123 alive / 86 gold
- HTTPS: 131 alive / 30 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 216 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46607
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
