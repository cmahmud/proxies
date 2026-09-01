# SyndProxy validated proxy pool

## Current pool

- Alive now: 660
- Gold now: 462
- HTTP: 126 alive / 91 gold
- HTTPS: 133 alive / 34 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 223 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46523
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
