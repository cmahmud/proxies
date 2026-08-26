# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 396
- HTTP: 145 alive / 69 gold
- HTTPS: 125 alive / 23 gold
- SOCKS4: 168 alive / 149 gold
- SOCKS5: 194 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39576
- Ever gold: 1299

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
