# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 461
- HTTP: 128 alive / 88 gold
- HTTPS: 113 alive / 34 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 191 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46726
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
