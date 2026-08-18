# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 369
- HTTP: 302 alive / 62 gold
- HTTPS: 229 alive / 15 gold
- SOCKS4: 242 alive / 151 gold
- SOCKS5: 238 alive / 141 gold

## Historical pool

- Discovered: 107156
- Ever alive: 15155
- Ever gold: 488

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
