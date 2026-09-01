# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 464
- HTTP: 135 alive / 95 gold
- HTTPS: 126 alive / 32 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 185 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46674
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
