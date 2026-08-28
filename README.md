# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 439
- HTTP: 128 alive / 86 gold
- HTTPS: 148 alive / 19 gold
- SOCKS4: 177 alive / 164 gold
- SOCKS5: 197 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42239
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
