# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 348
- HTTP: 167 alive / 40 gold
- HTTPS: 49 alive / 9 gold
- SOCKS4: 183 alive / 154 gold
- SOCKS5: 241 alive / 145 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32873
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
