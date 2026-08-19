# SyndProxy private pool

## Current pool

- Alive now: 980
- Gold now: 495
- HTTP: 316 alive / 148 gold
- HTTPS: 229 alive / 89 gold
- SOCKS4: 210 alive / 122 gold
- SOCKS5: 225 alive / 136 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17578
- Ever gold: 690

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
