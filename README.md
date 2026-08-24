# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 416
- HTTP: 117 alive / 75 gold
- HTTPS: 67 alive / 19 gold
- SOCKS4: 162 alive / 159 gold
- SOCKS5: 188 alive / 163 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33757
- Ever gold: 1250

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
