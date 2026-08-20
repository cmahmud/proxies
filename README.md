# SyndProxy private pool

## Current pool

- Alive now: 813
- Gold now: 367
- HTTP: 241 alive / 68 gold
- HTTPS: 154 alive / 16 gold
- SOCKS4: 211 alive / 148 gold
- SOCKS5: 207 alive / 135 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25487
- Ever gold: 1060

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
