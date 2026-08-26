# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 416
- HTTP: 102 alive / 68 gold
- HTTPS: 88 alive / 19 gold
- SOCKS4: 172 alive / 164 gold
- SOCKS5: 174 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37818
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
