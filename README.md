# SyndProxy private pool

## Current pool

- Alive now: 716
- Gold now: 377
- HTTP: 173 alive / 60 gold
- HTTPS: 112 alive / 18 gold
- SOCKS4: 202 alive / 149 gold
- SOCKS5: 229 alive / 150 gold

## Historical pool

- Discovered: 147647
- Ever alive: 25862
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
