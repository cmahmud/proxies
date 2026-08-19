# SyndProxy private pool

## Current pool

- Alive now: 905
- Gold now: 300
- HTTP: 307 alive / 65 gold
- HTTPS: 225 alive / 17 gold
- SOCKS4: 196 alive / 118 gold
- SOCKS5: 177 alive / 100 gold

## Historical pool

- Discovered: 109987
- Ever alive: 15622
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
