# SyndProxy private pool

## Current pool

- Alive now: 1346
- Gold now: 440
- HTTP: 464 alive / 100 gold
- HTTPS: 351 alive / 27 gold
- SOCKS4: 251 alive / 151 gold
- SOCKS5: 280 alive / 162 gold

## Historical pool

- Discovered: 159282
- Ever alive: 30462
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
