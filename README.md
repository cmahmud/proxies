# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 402
- HTTP: 91 alive / 63 gold
- HTTPS: 82 alive / 18 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 173 alive / 161 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37643
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
