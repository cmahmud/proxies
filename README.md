# SyndProxy private pool

## Current pool

- Alive now: 731
- Gold now: 368
- HTTP: 199 alive / 69 gold
- HTTPS: 115 alive / 15 gold
- SOCKS4: 210 alive / 148 gold
- SOCKS5: 207 alive / 136 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25480
- Ever gold: 1060

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
