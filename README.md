# SyndProxy private pool

## Current pool

- Alive now: 727
- Gold now: 247
- HTTP: 183 alive / 25 gold
- HTTPS: 157 alive / 9 gold
- SOCKS4: 180 alive / 111 gold
- SOCKS5: 207 alive / 102 gold

## Historical pool

- Discovered: 95261
- Ever alive: 10224
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
