# SyndProxy private pool

## Current pool

- Alive now: 811
- Gold now: 413
- HTTP: 252 alive / 92 gold
- HTTPS: 141 alive / 23 gold
- SOCKS4: 209 alive / 146 gold
- SOCKS5: 209 alive / 152 gold

## Historical pool

- Discovered: 152160
- Ever alive: 27830
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
