# SyndProxy private pool

## Current pool

- Alive now: 743
- Gold now: 387
- HTTP: 154 alive / 78 gold
- HTTPS: 165 alive / 22 gold
- SOCKS4: 199 alive / 127 gold
- SOCKS5: 225 alive / 160 gold

## Historical pool

- Discovered: 150719
- Ever alive: 27079
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
