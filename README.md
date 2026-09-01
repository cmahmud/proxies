# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 447
- HTTP: 105 alive / 79 gold
- HTTPS: 107 alive / 30 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 188 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47387
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
