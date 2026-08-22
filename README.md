# SyndProxy private pool

## Current pool

- Alive now: 1101
- Gold now: 371
- HTTP: 395 alive / 79 gold
- HTTPS: 274 alive / 24 gold
- SOCKS4: 171 alive / 105 gold
- SOCKS5: 261 alive / 163 gold

## Historical pool

- Discovered: 166635
- Ever alive: 32471
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
