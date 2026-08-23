# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 332
- HTTP: 112 alive / 37 gold
- HTTPS: 61 alive / 9 gold
- SOCKS4: 171 alive / 147 gold
- SOCKS5: 173 alive / 139 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32792
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
