# SyndProxy private pool

## Current pool

- Alive now: 1111
- Gold now: 497
- HTTP: 439 alive / 177 gold
- HTTPS: 262 alive / 100 gold
- SOCKS4: 222 alive / 109 gold
- SOCKS5: 188 alive / 111 gold

## Historical pool

- Discovered: 124845
- Ever alive: 19337
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
