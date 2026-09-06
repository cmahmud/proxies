# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 416
- HTTP: 119 alive / 84 gold
- HTTPS: 62 alive / 27 gold
- SOCKS4: 168 alive / 147 gold
- SOCKS5: 188 alive / 158 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48048
- Ever gold: 1516

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
