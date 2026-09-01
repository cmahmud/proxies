# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 466
- HTTP: 127 alive / 91 gold
- HTTPS: 123 alive / 37 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 219 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46487
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
