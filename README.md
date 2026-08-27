# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 428
- HTTP: 115 alive / 80 gold
- HTTPS: 123 alive / 20 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42164
- Ever gold: 1352

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
