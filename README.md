# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 397
- HTTP: 146 alive / 66 gold
- HTTPS: 71 alive / 14 gold
- SOCKS4: 170 alive / 155 gold
- SOCKS5: 192 alive / 162 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33287
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
