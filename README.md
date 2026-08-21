# SyndProxy private pool

## Current pool

- Alive now: 910
- Gold now: 413
- HTTP: 259 alive / 83 gold
- HTTPS: 193 alive / 25 gold
- SOCKS4: 214 alive / 150 gold
- SOCKS5: 244 alive / 155 gold

## Historical pool

- Discovered: 154658
- Ever alive: 28920
- Ever gold: 1115

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
