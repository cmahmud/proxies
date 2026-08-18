# SyndProxy private pool

## Current pool

- Alive now: 988
- Gold now: 368
- HTTP: 299 alive / 62 gold
- HTTPS: 219 alive / 15 gold
- SOCKS4: 237 alive / 150 gold
- SOCKS5: 233 alive / 141 gold

## Historical pool

- Discovered: 107156
- Ever alive: 15144
- Ever gold: 488

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
