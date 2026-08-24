# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 441
- HTTP: 128 alive / 83 gold
- HTTPS: 80 alive / 24 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 182 alive / 173 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34715
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
