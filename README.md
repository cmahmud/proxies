# SyndProxy validated proxy pool

## Current pool

- Alive now: 655
- Gold now: 466
- HTTP: 131 alive / 91 gold
- HTTPS: 125 alive / 36 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 220 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46492
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
