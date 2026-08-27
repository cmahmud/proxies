# SyndProxy validated proxy pool

## Current pool

- Alive now: 600
- Gold now: 427
- HTTP: 110 alive / 80 gold
- HTTPS: 128 alive / 20 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42160
- Ever gold: 1352

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
