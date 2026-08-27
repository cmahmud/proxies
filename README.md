# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 410
- HTTP: 103 alive / 65 gold
- HTTPS: 154 alive / 17 gold
- SOCKS4: 183 alive / 160 gold
- SOCKS5: 194 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41113
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
