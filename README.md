# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 400
- HTTP: 99 alive / 58 gold
- HTTPS: 66 alive / 15 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39060
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
