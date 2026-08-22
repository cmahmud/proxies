# SyndProxy private pool

## Current pool

- Alive now: 834
- Gold now: 404
- HTTP: 207 alive / 86 gold
- HTTPS: 181 alive / 29 gold
- SOCKS4: 217 alive / 134 gold
- SOCKS5: 229 alive / 155 gold

## Historical pool

- Discovered: 163855
- Ever alive: 31949
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
