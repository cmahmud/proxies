# SyndProxy private pool

## Current pool

- Alive now: 622
- Gold now: 264
- HTTP: 170 alive / 35 gold
- HTTPS: 80 alive / 10 gold
- SOCKS4: 191 alive / 137 gold
- SOCKS5: 181 alive / 82 gold

## Historical pool

- Discovered: 94350
- Ever alive: 9687
- Ever gold: 373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
