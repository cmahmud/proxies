# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 424
- HTTP: 111 alive / 77 gold
- HTTPS: 133 alive / 21 gold
- SOCKS4: 179 alive / 158 gold
- SOCKS5: 196 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42364
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
