# SyndProxy validated proxy pool

## Current pool

- Alive now: 419
- Gold now: 356
- HTTP: 52 alive / 34 gold
- HTTPS: 32 alive / 5 gold
- SOCKS4: 163 alive / 157 gold
- SOCKS5: 172 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43556
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
