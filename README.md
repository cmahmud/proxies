# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 400
- HTTP: 87 alive / 64 gold
- HTTPS: 71 alive / 19 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 171 alive / 158 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37648
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
