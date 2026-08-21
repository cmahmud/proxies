# SyndProxy private pool

## Current pool

- Alive now: 1156
- Gold now: 426
- HTTP: 381 alive / 98 gold
- HTTPS: 284 alive / 26 gold
- SOCKS4: 217 alive / 147 gold
- SOCKS5: 274 alive / 155 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28226
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
