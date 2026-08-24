# SyndProxy validated proxy pool

## Current pool

- Alive now: 604
- Gold now: 430
- HTTP: 134 alive / 75 gold
- HTTPS: 105 alive / 24 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 189 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34637
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
