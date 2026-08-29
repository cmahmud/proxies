# SyndProxy validated proxy pool

## Current pool

- Alive now: 434
- Gold now: 347
- HTTP: 84 alive / 45 gold
- HTTPS: 43 alive / 10 gold
- SOCKS4: 155 alive / 147 gold
- SOCKS5: 152 alive / 145 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43639
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
