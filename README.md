# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 399
- HTTP: 111 alive / 69 gold
- HTTPS: 61 alive / 26 gold
- SOCKS4: 160 alive / 149 gold
- SOCKS5: 170 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43653
- Ever gold: 1376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
