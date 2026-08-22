# SyndProxy private pool

## Current pool

- Alive now: 1074
- Gold now: 422
- HTTP: 324 alive / 92 gold
- HTTPS: 219 alive / 23 gold
- SOCKS4: 241 alive / 140 gold
- SOCKS5: 290 alive / 167 gold

## Historical pool

- Discovered: 164947
- Ever alive: 32223
- Ever gold: 1174

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
