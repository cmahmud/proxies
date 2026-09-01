# SyndProxy validated proxy pool

## Current pool

- Alive now: 658
- Gold now: 462
- HTTP: 124 alive / 91 gold
- HTTPS: 134 alive / 34 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 221 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46521
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
