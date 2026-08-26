# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 381
- HTTP: 128 alive / 64 gold
- HTTPS: 160 alive / 21 gold
- SOCKS4: 160 alive / 146 gold
- SOCKS5: 174 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39683
- Ever gold: 1301

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
