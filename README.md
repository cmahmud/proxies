# SyndProxy private pool

## Current pool

- Alive now: 1156
- Gold now: 427
- HTTP: 368 alive / 98 gold
- HTTPS: 294 alive / 27 gold
- SOCKS4: 220 alive / 147 gold
- SOCKS5: 274 alive / 155 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28230
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
