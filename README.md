# SyndProxy validated proxy pool

## Current pool

- Alive now: 334
- Gold now: 225
- HTTP: 34 alive / 20 gold
- HTTPS: 1 alive / 0 gold
- SOCKS4: 149 alive / 105 gold
- SOCKS5: 150 alive / 100 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43626
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
