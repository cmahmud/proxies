# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 397
- HTTP: 83 alive / 58 gold
- HTTPS: 94 alive / 16 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 176 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42937
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
