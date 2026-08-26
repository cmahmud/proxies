# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 397
- HTTP: 129 alive / 73 gold
- HTTPS: 152 alive / 16 gold
- SOCKS4: 160 alive / 151 gold
- SOCKS5: 182 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40194
- Ever gold: 1307

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
