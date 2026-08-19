# SyndProxy private pool

## Current pool

- Alive now: 1195
- Gold now: 393
- HTTP: 383 alive / 89 gold
- HTTPS: 231 alive / 17 gold
- SOCKS4: 246 alive / 144 gold
- SOCKS5: 335 alive / 143 gold

## Historical pool

- Discovered: 133967
- Ever alive: 21720
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
