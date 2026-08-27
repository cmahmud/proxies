# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 403
- HTTP: 90 alive / 64 gold
- HTTPS: 76 alive / 17 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41743
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
