# SyndProxy validated proxy pool

## Current pool

- Alive now: 330
- Gold now: 256
- HTTP: 31 alive / 21 gold
- HTTPS: 2 alive / 0 gold
- SOCKS4: 148 alive / 128 gold
- SOCKS5: 149 alive / 107 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43625
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
