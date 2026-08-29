# SyndProxy validated proxy pool

## Current pool

- Alive now: 373
- Gold now: 333
- HTTP: 45 alive / 28 gold
- HTTPS: 6 alive / 0 gold
- SOCKS4: 158 alive / 155 gold
- SOCKS5: 164 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43602
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
