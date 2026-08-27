# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 408
- HTTP: 113 alive / 64 gold
- HTTPS: 154 alive / 14 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 195 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41118
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
