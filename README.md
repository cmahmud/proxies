# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 440
- HTTP: 128 alive / 89 gold
- HTTPS: 132 alive / 21 gold
- SOCKS4: 184 alive / 160 gold
- SOCKS5: 199 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42209
- Ever gold: 1354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
