# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 432
- HTTP: 110 alive / 81 gold
- HTTPS: 129 alive / 22 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 194 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42290
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
