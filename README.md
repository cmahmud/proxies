# SyndProxy validated proxy pool

## Current pool

- Alive now: 418
- Gold now: 337
- HTTP: 53 alive / 33 gold
- HTTPS: 35 alive / 5 gold
- SOCKS4: 159 alive / 150 gold
- SOCKS5: 171 alive / 149 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43562
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
