# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 407
- HTTP: 111 alive / 63 gold
- HTTPS: 128 alive / 14 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41339
- Ever gold: 1325

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
