# SyndProxy private pool

## Current pool

- Alive now: 1035
- Gold now: 371
- HTTP: 362 alive / 77 gold
- HTTPS: 250 alive / 25 gold
- SOCKS4: 172 alive / 105 gold
- SOCKS5: 251 alive / 164 gold

## Historical pool

- Discovered: 166635
- Ever alive: 32471
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
