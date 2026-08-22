# SyndProxy private pool

## Current pool

- Alive now: 777
- Gold now: 413
- HTTP: 200 alive / 92 gold
- HTTPS: 132 alive / 26 gold
- SOCKS4: 200 alive / 132 gold
- SOCKS5: 245 alive / 163 gold

## Historical pool

- Discovered: 163856
- Ever alive: 31959
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
