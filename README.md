# SyndProxy validated proxy pool

## Current pool

- Alive now: 392
- Gold now: 201
- HTTP: 131 alive / 40 gold
- HTTPS: 64 alive / 8 gold
- SOCKS4: 73 alive / 64 gold
- SOCKS5: 124 alive / 89 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32718
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
