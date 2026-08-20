# SyndProxy private pool

## Current pool

- Alive now: 747
- Gold now: 374
- HTTP: 215 alive / 70 gold
- HTTPS: 116 alive / 21 gold
- SOCKS4: 225 alive / 143 gold
- SOCKS5: 191 alive / 140 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25495
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
