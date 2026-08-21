# SyndProxy private pool

## Current pool

- Alive now: 833
- Gold now: 413
- HTTP: 221 alive / 92 gold
- HTTPS: 165 alive / 25 gold
- SOCKS4: 205 alive / 146 gold
- SOCKS5: 242 alive / 150 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29118
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
