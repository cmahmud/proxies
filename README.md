# SyndProxy validated proxy pool

## Current pool

- Alive now: 661
- Gold now: 421
- HTTP: 150 alive / 80 gold
- HTTPS: 157 alive / 26 gold
- SOCKS4: 165 alive / 153 gold
- SOCKS5: 189 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40280
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
