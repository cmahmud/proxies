# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 424
- HTTP: 121 alive / 80 gold
- HTTPS: 152 alive / 15 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42308
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
