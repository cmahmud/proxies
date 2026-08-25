# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 418
- HTTP: 107 alive / 66 gold
- HTTPS: 87 alive / 19 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 199 alive / 172 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36045
- Ever gold: 1265

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
