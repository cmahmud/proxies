# SyndProxy private pool

## Current pool

- Alive now: 766
- Gold now: 379
- HTTP: 224 alive / 72 gold
- HTTPS: 113 alive / 22 gold
- SOCKS4: 227 alive / 143 gold
- SOCKS5: 202 alive / 142 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25500
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
