# SyndProxy private pool

## Current pool

- Alive now: 1177
- Gold now: 491
- HTTP: 389 alive / 120 gold
- HTTPS: 268 alive / 70 gold
- SOCKS4: 232 alive / 153 gold
- SOCKS5: 288 alive / 148 gold

## Historical pool

- Discovered: 114413
- Ever alive: 17047
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
