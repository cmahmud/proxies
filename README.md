# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 403
- HTTP: 102 alive / 57 gold
- HTTPS: 151 alive / 13 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 194 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40768
- Ever gold: 1312

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
