# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 428
- HTTP: 111 alive / 78 gold
- HTTPS: 151 alive / 19 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42324
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
