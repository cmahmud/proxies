# SyndProxy private pool

## Current pool

- Alive now: 714
- Gold now: 245
- HTTP: 174 alive / 24 gold
- HTTPS: 151 alive / 8 gold
- SOCKS4: 180 alive / 111 gold
- SOCKS5: 209 alive / 102 gold

## Historical pool

- Discovered: 95261
- Ever alive: 10224
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
