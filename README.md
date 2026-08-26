# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 411
- HTTP: 96 alive / 63 gold
- HTTPS: 73 alive / 18 gold
- SOCKS4: 181 alive / 160 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39102
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
