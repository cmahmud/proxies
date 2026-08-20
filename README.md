# SyndProxy private pool

## Current pool

- Alive now: 831
- Gold now: 422
- HTTP: 207 alive / 81 gold
- HTTPS: 160 alive / 29 gold
- SOCKS4: 235 alive / 152 gold
- SOCKS5: 229 alive / 160 gold

## Historical pool

- Discovered: 151059
- Ever alive: 27309
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
