# SyndProxy private pool

## Current pool

- Alive now: 963
- Gold now: 389
- HTTP: 287 alive / 86 gold
- HTTPS: 191 alive / 27 gold
- SOCKS4: 240 alive / 143 gold
- SOCKS5: 245 alive / 133 gold

## Historical pool

- Discovered: 160993
- Ever alive: 30901
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
