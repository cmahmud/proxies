# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 399
- HTTP: 110 alive / 74 gold
- HTTPS: 78 alive / 12 gold
- SOCKS4: 157 alive / 155 gold
- SOCKS5: 167 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43116
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
