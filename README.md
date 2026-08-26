# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 386
- HTTP: 113 alive / 62 gold
- HTTPS: 97 alive / 20 gold
- SOCKS4: 169 alive / 150 gold
- SOCKS5: 188 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39335
- Ever gold: 1298

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
