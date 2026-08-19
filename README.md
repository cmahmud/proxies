# SyndProxy private pool

## Current pool

- Alive now: 1055
- Gold now: 507
- HTTP: 388 alive / 152 gold
- HTTPS: 268 alive / 87 gold
- SOCKS4: 186 alive / 115 gold
- SOCKS5: 213 alive / 153 gold

## Historical pool

- Discovered: 117177
- Ever alive: 17741
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
