# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 393
- HTTP: 87 alive / 50 gold
- HTTPS: 60 alive / 18 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41609
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
