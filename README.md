# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 413
- HTTP: 93 alive / 65 gold
- HTTPS: 82 alive / 20 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35504
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
