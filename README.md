# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 397
- HTTP: 134 alive / 75 gold
- HTTPS: 181 alive / 22 gold
- SOCKS4: 159 alive / 145 gold
- SOCKS5: 177 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39994
- Ever gold: 1305

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
