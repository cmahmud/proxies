# SyndProxy private pool

## Current pool

- Alive now: 943
- Gold now: 417
- HTTP: 292 alive / 91 gold
- HTTPS: 176 alive / 24 gold
- SOCKS4: 215 alive / 141 gold
- SOCKS5: 260 alive / 161 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29037
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
