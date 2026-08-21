# SyndProxy private pool

## Current pool

- Alive now: 799
- Gold now: 407
- HTTP: 215 alive / 95 gold
- HTTPS: 145 alive / 24 gold
- SOCKS4: 204 alive / 136 gold
- SOCKS5: 235 alive / 152 gold

## Historical pool

- Discovered: 154732
- Ever alive: 29174
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
