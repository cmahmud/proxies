# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 373
- HTTP: 104 alive / 64 gold
- HTTPS: 61 alive / 15 gold
- SOCKS4: 155 alive / 143 gold
- SOCKS5: 178 alive / 151 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38793
- Ever gold: 1292

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
