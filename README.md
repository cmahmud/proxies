# SyndProxy private pool

## Current pool

- Alive now: 754
- Gold now: 380
- HTTP: 203 alive / 77 gold
- HTTPS: 124 alive / 19 gold
- SOCKS4: 225 alive / 146 gold
- SOCKS5: 202 alive / 138 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25490
- Ever gold: 1061

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
