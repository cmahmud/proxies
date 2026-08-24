# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 383
- HTTP: 119 alive / 61 gold
- HTTPS: 53 alive / 15 gold
- SOCKS4: 169 alive / 154 gold
- SOCKS5: 178 alive / 153 gold

## Historical pool

- Discovered: 176968
- Ever alive: 33255
- Ever gold: 1232

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
