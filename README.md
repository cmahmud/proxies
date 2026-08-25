# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 395
- HTTP: 93 alive / 63 gold
- HTTPS: 74 alive / 17 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 171 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37547
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
