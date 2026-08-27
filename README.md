# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 412
- HTTP: 112 alive / 64 gold
- HTTPS: 165 alive / 17 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40791
- Ever gold: 1312

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
