# SyndProxy private pool

## Current pool

- Alive now: 1080
- Gold now: 366
- HTTP: 375 alive / 73 gold
- HTTPS: 266 alive / 11 gold
- SOCKS4: 208 alive / 128 gold
- SOCKS5: 231 alive / 154 gold

## Historical pool

- Discovered: 129304
- Ever alive: 20377
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
