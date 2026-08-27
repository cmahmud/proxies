# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 405
- HTTP: 110 alive / 63 gold
- HTTPS: 158 alive / 13 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41133
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
