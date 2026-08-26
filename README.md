# SyndProxy validated proxy pool

## Current pool

- Alive now: 468
- Gold now: 370
- HTTP: 85 alive / 60 gold
- HTTPS: 57 alive / 16 gold
- SOCKS4: 155 alive / 142 gold
- SOCKS5: 171 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38877
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
