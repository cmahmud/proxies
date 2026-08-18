# SyndProxy private pool

## Current pool

- Alive now: 1057
- Gold now: 285
- HTTP: 368 alive / 27 gold
- HTTPS: 216 alive / 4 gold
- SOCKS4: 228 alive / 136 gold
- SOCKS5: 245 alive / 118 gold

## Historical pool

- Discovered: 102805
- Ever alive: 12701
- Ever gold: 399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
