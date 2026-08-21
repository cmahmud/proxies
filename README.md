# SyndProxy private pool

## Current pool

- Alive now: 833
- Gold now: 413
- HTTP: 229 alive / 91 gold
- HTTPS: 158 alive / 28 gold
- SOCKS4: 214 alive / 146 gold
- SOCKS5: 232 alive / 148 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29129
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
