# SyndProxy private pool

## Current pool

- Alive now: 1177
- Gold now: 492
- HTTP: 384 alive / 121 gold
- HTTPS: 278 alive / 70 gold
- SOCKS4: 229 alive / 153 gold
- SOCKS5: 286 alive / 148 gold

## Historical pool

- Discovered: 114413
- Ever alive: 17045
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
