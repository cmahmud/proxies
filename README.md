# SyndProxy private pool

## Current pool

- Alive now: 888
- Gold now: 302
- HTTP: 308 alive / 64 gold
- HTTPS: 200 alive / 18 gold
- SOCKS4: 202 alive / 118 gold
- SOCKS5: 178 alive / 102 gold

## Historical pool

- Discovered: 109987
- Ever alive: 15624
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
