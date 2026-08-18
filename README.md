# SyndProxy private pool

## Current pool

- Alive now: 732
- Gold now: 245
- HTTP: 184 alive / 25 gold
- HTTPS: 162 alive / 9 gold
- SOCKS4: 179 alive / 108 gold
- SOCKS5: 207 alive / 103 gold

## Historical pool

- Discovered: 95261
- Ever alive: 10224
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
