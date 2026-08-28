# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 422
- HTTP: 94 alive / 71 gold
- HTTPS: 106 alive / 21 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 180 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42559
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
