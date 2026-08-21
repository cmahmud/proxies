# SyndProxy private pool

## Current pool

- Alive now: 810
- Gold now: 364
- HTTP: 231 alive / 77 gold
- HTTPS: 152 alive / 19 gold
- SOCKS4: 191 alive / 131 gold
- SOCKS5: 236 alive / 137 gold

## Historical pool

- Discovered: 156840
- Ever alive: 29643
- Ever gold: 1134

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
