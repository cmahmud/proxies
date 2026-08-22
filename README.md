# SyndProxy private pool

## Current pool

- Alive now: 772
- Gold now: 413
- HTTP: 198 alive / 87 gold
- HTTPS: 142 alive / 29 gold
- SOCKS4: 205 alive / 140 gold
- SOCKS5: 227 alive / 157 gold

## Historical pool

- Discovered: 163857
- Ever alive: 31960
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
