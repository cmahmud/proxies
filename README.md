# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 410
- HTTP: 123 alive / 68 gold
- HTTPS: 154 alive / 13 gold
- SOCKS4: 182 alive / 159 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40847
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
