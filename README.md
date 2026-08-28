# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 411
- HTTP: 98 alive / 62 gold
- HTTPS: 93 alive / 24 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 181 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42990
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
