# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 413
- HTTP: 314 alive / 90 gold
- HTTPS: 212 alive / 20 gold
- SOCKS4: 223 alive / 141 gold
- SOCKS5: 266 alive / 162 gold

## Historical pool

- Discovered: 136195
- Ever alive: 22309
- Ever gold: 896

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
