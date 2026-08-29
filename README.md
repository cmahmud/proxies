# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 358
- HTTP: 90 alive / 63 gold
- HTTPS: 85 alive / 15 gold
- SOCKS4: 160 alive / 143 gold
- SOCKS5: 173 alive / 137 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43324
- Ever gold: 1369

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
