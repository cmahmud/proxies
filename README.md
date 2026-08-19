# SyndProxy private pool

## Current pool

- Alive now: 918
- Gold now: 300
- HTTP: 336 alive / 64 gold
- HTTPS: 204 alive / 17 gold
- SOCKS4: 201 alive / 118 gold
- SOCKS5: 177 alive / 101 gold

## Historical pool

- Discovered: 109987
- Ever alive: 15624
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
