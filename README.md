# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 446
- HTTP: 115 alive / 84 gold
- HTTPS: 50 alive / 31 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 180 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43679
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
