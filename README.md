# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 448
- HTTP: 108 alive / 78 gold
- HTTPS: 109 alive / 29 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 188 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47369
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
