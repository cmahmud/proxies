# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 407
- HTTP: 88 alive / 59 gold
- HTTPS: 55 alive / 22 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 186 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41713
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
