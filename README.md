# SyndProxy private pool

## Current pool

- Alive now: 977
- Gold now: 413
- HTTP: 315 alive / 104 gold
- HTTPS: 209 alive / 25 gold
- SOCKS4: 228 alive / 154 gold
- SOCKS5: 225 alive / 130 gold

## Historical pool

- Discovered: 160980
- Ever alive: 30831
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
