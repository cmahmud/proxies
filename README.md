# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 393
- HTTP: 78 alive / 52 gold
- HTTPS: 40 alive / 16 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 186 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42855
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
