# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 416
- HTTP: 100 alive / 62 gold
- HTTPS: 95 alive / 24 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 191 alive / 169 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35795
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
