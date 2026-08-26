# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 372
- HTTP: 95 alive / 57 gold
- HTTPS: 59 alive / 20 gold
- SOCKS4: 155 alive / 142 gold
- SOCKS5: 171 alive / 153 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38853
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
