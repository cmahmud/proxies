# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 398
- HTTP: 95 alive / 55 gold
- HTTPS: 104 alive / 15 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 192 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41501
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
