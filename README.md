# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 408
- HTTP: 110 alive / 66 gold
- HTTPS: 165 alive / 16 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41078
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
