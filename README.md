# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 444
- HTTP: 117 alive / 83 gold
- HTTPS: 64 alive / 28 gold
- SOCKS4: 169 alive / 163 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43691
- Ever gold: 1378

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
