# SyndProxy validated proxy pool

## Current pool

- Alive now: 611
- Gold now: 437
- HTTP: 134 alive / 81 gold
- HTTPS: 108 alive / 23 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 193 alive / 173 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34533
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
