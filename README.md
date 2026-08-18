# SyndProxy private pool

## Current pool

- Alive now: 986
- Gold now: 370
- HTTP: 298 alive / 62 gold
- HTTPS: 212 alive / 15 gold
- SOCKS4: 239 alive / 151 gold
- SOCKS5: 237 alive / 142 gold

## Historical pool

- Discovered: 107156
- Ever alive: 15155
- Ever gold: 488

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
