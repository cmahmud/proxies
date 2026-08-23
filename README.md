# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 348
- HTTP: 177 alive / 40 gold
- HTTPS: 49 alive / 9 gold
- SOCKS4: 178 alive / 154 gold
- SOCKS5: 237 alive / 145 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32873
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
