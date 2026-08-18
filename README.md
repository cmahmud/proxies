# SyndProxy private pool

## Current pool

- Alive now: 1059
- Gold now: 320
- HTTP: 364 alive / 42 gold
- HTTPS: 206 alive / 11 gold
- SOCKS4: 252 alive / 138 gold
- SOCKS5: 237 alive / 129 gold

## Historical pool

- Discovered: 107043
- Ever alive: 14390
- Ever gold: 442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
