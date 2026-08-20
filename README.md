# SyndProxy private pool

## Current pool

- Alive now: 813
- Gold now: 381
- HTTP: 241 alive / 75 gold
- HTTPS: 137 alive / 18 gold
- SOCKS4: 230 alive / 146 gold
- SOCKS5: 205 alive / 142 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25493
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
