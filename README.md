# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 413
- HTTP: 98 alive / 63 gold
- HTTPS: 88 alive / 22 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35475
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
