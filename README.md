# SyndProxy private pool

## Current pool

- Alive now: 963
- Gold now: 319
- HTTP: 290 alive / 35 gold
- HTTPS: 206 alive / 10 gold
- SOCKS4: 229 alive / 142 gold
- SOCKS5: 238 alive / 132 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14219
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
