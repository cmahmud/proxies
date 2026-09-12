# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 420
- HTTP: 115 alive / 75 gold
- HTTPS: 43 alive / 23 gold
- SOCKS4: 181 alive / 160 gold
- SOCKS5: 186 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49474
- Ever gold: 1584

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
