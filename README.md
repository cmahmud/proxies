# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 378
- HTTP: 111 alive / 66 gold
- HTTPS: 43 alive / 14 gold
- SOCKS4: 169 alive / 149 gold
- SOCKS5: 178 alive / 149 gold

## Historical pool

- Discovered: 176956
- Ever alive: 33251
- Ever gold: 1232

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
