# SyndProxy private pool

## Current pool

- Alive now: 629
- Gold now: 260
- HTTP: 167 alive / 35 gold
- HTTPS: 87 alive / 10 gold
- SOCKS4: 194 alive / 133 gold
- SOCKS5: 181 alive / 82 gold

## Historical pool

- Discovered: 94350
- Ever alive: 9687
- Ever gold: 373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
