# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 378
- HTTP: 104 alive / 60 gold
- HTTPS: 62 alive / 19 gold
- SOCKS4: 150 alive / 144 gold
- SOCKS5: 174 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38910
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
