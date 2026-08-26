# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 382
- HTTP: 101 alive / 68 gold
- HTTPS: 54 alive / 19 gold
- SOCKS4: 153 alive / 143 gold
- SOCKS5: 175 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38786
- Ever gold: 1292

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
