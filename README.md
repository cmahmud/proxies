# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 394
- HTTP: 91 alive / 66 gold
- HTTPS: 84 alive / 16 gold
- SOCKS4: 163 alive / 152 gold
- SOCKS5: 169 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43339
- Ever gold: 1369

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
