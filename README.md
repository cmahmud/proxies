# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 383
- HTTP: 131 alive / 62 gold
- HTTPS: 59 alive / 16 gold
- SOCKS4: 168 alive / 154 gold
- SOCKS5: 169 alive / 151 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33210
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
