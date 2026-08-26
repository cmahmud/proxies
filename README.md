# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 372
- HTTP: 83 alive / 60 gold
- HTTPS: 55 alive / 17 gold
- SOCKS4: 157 alive / 143 gold
- SOCKS5: 171 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38877
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
