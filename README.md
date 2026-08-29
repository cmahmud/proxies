# SyndProxy validated proxy pool

## Current pool

- Alive now: 334
- Gold now: 308
- HTTP: 35 alive / 26 gold
- HTTPS: 1 alive / 0 gold
- SOCKS4: 150 alive / 147 gold
- SOCKS5: 148 alive / 135 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43624
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
