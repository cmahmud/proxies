# SyndProxy private pool

## Current pool

- Alive now: 855
- Gold now: 290
- HTTP: 234 alive / 28 gold
- HTTPS: 124 alive / 5 gold
- SOCKS4: 254 alive / 142 gold
- SOCKS5: 243 alive / 115 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12180
- Ever gold: 396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
