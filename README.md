# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 399
- HTTP: 86 alive / 56 gold
- HTTPS: 95 alive / 20 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 170 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42968
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
