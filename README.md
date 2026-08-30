# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 455
- HTTP: 114 alive / 92 gold
- HTTPS: 55 alive / 31 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 178 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43676
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
