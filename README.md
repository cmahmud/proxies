# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 411
- HTTP: 113 alive / 64 gold
- HTTPS: 170 alive / 17 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40793
- Ever gold: 1312

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
