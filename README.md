# SyndProxy private pool

## Current pool

- Alive now: 943
- Gold now: 398
- HTTP: 261 alive / 82 gold
- HTTPS: 197 alive / 22 gold
- SOCKS4: 233 alive / 147 gold
- SOCKS5: 252 alive / 147 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29110
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
