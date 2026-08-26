# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 402
- HTTP: 102 alive / 59 gold
- HTTPS: 90 alive / 13 gold
- SOCKS4: 183 alive / 160 gold
- SOCKS5: 196 alive / 170 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38196
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
