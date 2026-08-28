# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 391
- HTTP: 75 alive / 55 gold
- HTTPS: 81 alive / 12 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 169 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42931
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
