# SyndProxy private pool

## Current pool

- Alive now: 1366
- Gold now: 413
- HTTP: 554 alive / 92 gold
- HTTPS: 338 alive / 36 gold
- SOCKS4: 230 alive / 140 gold
- SOCKS5: 244 alive / 145 gold

## Historical pool

- Discovered: 163250
- Ever alive: 31727
- Ever gold: 1165

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
