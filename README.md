# SyndProxy validated proxy pool

## Current pool

- Alive now: 393
- Gold now: 195
- HTTP: 134 alive / 39 gold
- HTTPS: 62 alive / 8 gold
- SOCKS4: 74 alive / 64 gold
- SOCKS5: 123 alive / 84 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32718
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
