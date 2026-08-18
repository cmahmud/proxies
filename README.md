# SyndProxy private pool

## Current pool

- Alive now: 1014
- Gold now: 371
- HTTP: 305 alive / 61 gold
- HTTPS: 223 alive / 15 gold
- SOCKS4: 248 alive / 152 gold
- SOCKS5: 238 alive / 143 gold

## Historical pool

- Discovered: 109322
- Ever alive: 15172
- Ever gold: 488

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
