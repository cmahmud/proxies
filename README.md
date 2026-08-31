# SyndProxy validated proxy pool

## Current pool

- Alive now: 696
- Gold now: 473
- HTTP: 174 alive / 95 gold
- HTTPS: 124 alive / 40 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 226 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45287
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
