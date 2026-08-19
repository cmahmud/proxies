# SyndProxy private pool

## Current pool

- Alive now: 1316
- Gold now: 596
- HTTP: 503 alive / 181 gold
- HTTPS: 344 alive / 113 gold
- SOCKS4: 243 alive / 145 gold
- SOCKS5: 226 alive / 157 gold

## Historical pool

- Discovered: 125238
- Ever alive: 19548
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
