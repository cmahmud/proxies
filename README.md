# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 413
- HTTP: 95 alive / 64 gold
- HTTPS: 90 alive / 19 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35518
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
