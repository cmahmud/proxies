# SyndProxy validated proxy pool

## Current pool

- Alive now: 386
- Gold now: 307
- HTTP: 50 alive / 29 gold
- HTTPS: 9 alive / 1 gold
- SOCKS4: 159 alive / 144 gold
- SOCKS5: 168 alive / 133 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43596
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
