# SyndProxy private pool

## Current pool

- Alive now: 1055
- Gold now: 378
- HTTP: 354 alive / 104 gold
- HTTPS: 229 alive / 31 gold
- SOCKS4: 207 alive / 111 gold
- SOCKS5: 265 alive / 132 gold

## Historical pool

- Discovered: 152755
- Ever alive: 28304
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
