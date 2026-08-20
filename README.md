# SyndProxy private pool

## Current pool

- Alive now: 1292
- Gold now: 565
- HTTP: 501 alive / 191 gold
- HTTPS: 354 alive / 92 gold
- SOCKS4: 215 alive / 148 gold
- SOCKS5: 222 alive / 134 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22940
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
