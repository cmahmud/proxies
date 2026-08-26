# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 411
- HTTP: 91 alive / 62 gold
- HTTPS: 69 alive / 18 gold
- SOCKS4: 183 alive / 161 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39104
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
