# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 452
- HTTP: 127 alive / 87 gold
- HTTPS: 121 alive / 31 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 214 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46593
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
