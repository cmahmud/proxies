# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 399
- HTTP: 74 alive / 51 gold
- HTTPS: 52 alive / 18 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41679
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
