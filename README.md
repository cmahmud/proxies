# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 373
- HTTP: 114 alive / 64 gold
- HTTPS: 73 alive / 15 gold
- SOCKS4: 150 alive / 143 gold
- SOCKS5: 181 alive / 151 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38802
- Ever gold: 1292

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
