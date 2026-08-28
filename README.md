# SyndProxy validated proxy pool

## Current pool

- Alive now: 452
- Gold now: 392
- HTTP: 75 alive / 55 gold
- HTTPS: 32 alive / 14 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 177 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42856
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
