# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 397
- HTTP: 105 alive / 59 gold
- HTTPS: 44 alive / 15 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 184 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38979
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
