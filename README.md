# SyndProxy private pool

## Current pool

- Alive now: 755
- Gold now: 377
- HTTP: 217 alive / 72 gold
- HTTPS: 114 alive / 22 gold
- SOCKS4: 225 alive / 143 gold
- SOCKS5: 199 alive / 140 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25496
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
