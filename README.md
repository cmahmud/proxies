# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 398
- HTTP: 118 alive / 64 gold
- HTTPS: 177 alive / 17 gold
- SOCKS4: 172 alive / 155 gold
- SOCKS5: 187 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40581
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
