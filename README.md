# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 411
- HTTP: 108 alive / 65 gold
- HTTPS: 160 alive / 17 gold
- SOCKS4: 183 alive / 161 gold
- SOCKS5: 195 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41111
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
