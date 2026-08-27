# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 408
- HTTP: 109 alive / 62 gold
- HTTPS: 162 alive / 18 gold
- SOCKS4: 183 alive / 161 gold
- SOCKS5: 195 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41105
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
