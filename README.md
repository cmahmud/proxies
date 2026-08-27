# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 412
- HTTP: 107 alive / 69 gold
- HTTPS: 178 alive / 22 gold
- SOCKS4: 171 alive / 156 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40572
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
