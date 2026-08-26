# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 406
- HTTP: 96 alive / 63 gold
- HTTPS: 74 alive / 15 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39179
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
