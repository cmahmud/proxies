# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 402
- HTTP: 88 alive / 62 gold
- HTTPS: 74 alive / 19 gold
- SOCKS4: 165 alive / 157 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38591
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
