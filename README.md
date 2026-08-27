# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 423
- HTTP: 107 alive / 78 gold
- HTTPS: 128 alive / 21 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42124
- Ever gold: 1351

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
