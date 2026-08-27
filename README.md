# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 416
- HTTP: 111 alive / 73 gold
- HTTPS: 112 alive / 23 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 183 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41845
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
