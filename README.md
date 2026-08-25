# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 402
- HTTP: 96 alive / 67 gold
- HTTPS: 68 alive / 19 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 172 alive / 157 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37228
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
