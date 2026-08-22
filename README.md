# SyndProxy private pool

## Current pool

- Alive now: 1055
- Gold now: 381
- HTTP: 346 alive / 85 gold
- HTTPS: 229 alive / 27 gold
- SOCKS4: 238 alive / 124 gold
- SOCKS5: 242 alive / 145 gold

## Historical pool

- Discovered: 164181
- Ever alive: 32049
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
