# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 408
- HTTP: 103 alive / 67 gold
- HTTPS: 115 alive / 18 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43007
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
