# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 407
- HTTP: 111 alive / 64 gold
- HTTPS: 153 alive / 18 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40888
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
