# SyndProxy validated proxy pool

## Current pool

- Alive now: 667
- Gold now: 407
- HTTP: 123 alive / 61 gold
- HTTPS: 182 alive / 12 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 187 alive / 174 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40818
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
