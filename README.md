# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 398
- HTTP: 105 alive / 61 gold
- HTTPS: 41 alive / 15 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 186 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38979
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
