# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 420
- HTTP: 110 alive / 78 gold
- HTTPS: 70 alive / 30 gold
- SOCKS4: 155 alive / 153 gold
- SOCKS5: 170 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43655
- Ever gold: 1376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
