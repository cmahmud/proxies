# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 423
- HTTP: 112 alive / 79 gold
- HTTPS: 61 alive / 29 gold
- SOCKS4: 159 alive / 154 gold
- SOCKS5: 172 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43655
- Ever gold: 1376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
