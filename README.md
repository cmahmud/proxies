# SyndProxy private pool

## Current pool

- Alive now: 993
- Gold now: 487
- HTTP: 319 alive / 148 gold
- HTTPS: 245 alive / 87 gold
- SOCKS4: 205 alive / 120 gold
- SOCKS5: 224 alive / 132 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17576
- Ever gold: 690

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
