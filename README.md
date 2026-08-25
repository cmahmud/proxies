# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 407
- HTTP: 93 alive / 67 gold
- HTTPS: 73 alive / 19 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 172 alive / 161 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37730
- Ever gold: 1287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
