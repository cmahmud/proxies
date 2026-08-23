# SyndProxy validated proxy pool

## Current pool

- Alive now: 314
- Gold now: 201
- HTTP: 103 alive / 37 gold
- HTTPS: 29 alive / 7 gold
- SOCKS4: 77 alive / 69 gold
- SOCKS5: 105 alive / 88 gold

## Historical pool

- Discovered: 170566
- Ever alive: 32765
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
