# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 418
- HTTP: 135 alive / 80 gold
- HTTPS: 155 alive / 23 gold
- SOCKS4: 168 alive / 154 gold
- SOCKS5: 182 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40235
- Ever gold: 1308

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
