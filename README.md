# SyndProxy private pool

## Current pool

- Alive now: 910
- Gold now: 388
- HTTP: 240 alive / 84 gold
- HTTPS: 211 alive / 22 gold
- SOCKS4: 218 alive / 127 gold
- SOCKS5: 241 alive / 155 gold

## Historical pool

- Discovered: 164909
- Ever alive: 32120
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
