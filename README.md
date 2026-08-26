# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 382
- HTTP: 130 alive / 68 gold
- HTTPS: 186 alive / 18 gold
- SOCKS4: 156 alive / 145 gold
- SOCKS5: 178 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39873
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
