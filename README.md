# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 395
- HTTP: 74 alive / 55 gold
- HTTPS: 81 alive / 15 gold
- SOCKS4: 167 alive / 162 gold
- SOCKS5: 179 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42899
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
