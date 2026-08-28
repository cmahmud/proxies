# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 393
- HTTP: 91 alive / 69 gold
- HTTPS: 81 alive / 12 gold
- SOCKS4: 160 alive / 154 gold
- SOCKS5: 169 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43140
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
