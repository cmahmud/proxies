# SyndProxy validated proxy pool

## Current pool

- Alive now: 419
- Gold now: 353
- HTTP: 49 alive / 32 gold
- HTTPS: 35 alive / 3 gold
- SOCKS4: 164 alive / 156 gold
- SOCKS5: 171 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43563
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
