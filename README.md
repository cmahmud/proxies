# SyndProxy private pool

## Current pool

- Alive now: 755
- Gold now: 388
- HTTP: 204 alive / 79 gold
- HTTPS: 159 alive / 20 gold
- SOCKS4: 201 alive / 147 gold
- SOCKS5: 191 alive / 142 gold

## Historical pool

- Discovered: 149514
- Ever alive: 26927
- Ever gold: 1089

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
