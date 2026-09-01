# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 462
- HTTP: 132 alive / 94 gold
- HTTPS: 124 alive / 30 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 187 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46674
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
