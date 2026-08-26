# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 372
- HTTP: 89 alive / 58 gold
- HTTPS: 57 alive / 17 gold
- SOCKS4: 159 alive / 143 gold
- SOCKS5: 171 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38887
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
