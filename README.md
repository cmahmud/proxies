# SyndProxy validated proxy pool

## Current pool

- Alive now: 380
- Gold now: 201
- HTTP: 123 alive / 40 gold
- HTTPS: 67 alive / 8 gold
- SOCKS4: 71 alive / 64 gold
- SOCKS5: 119 alive / 89 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32718
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
