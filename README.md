# SyndProxy validated proxy pool

## Current pool

- Alive now: 658
- Gold now: 398
- HTTP: 176 alive / 69 gold
- HTTPS: 115 alive / 22 gold
- SOCKS4: 165 alive / 150 gold
- SOCKS5: 202 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39504
- Ever gold: 1298

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
