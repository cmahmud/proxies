# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 406
- HTTP: 100 alive / 61 gold
- HTTPS: 159 alive / 17 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 195 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40723
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
