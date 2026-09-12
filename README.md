# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 420
- HTTP: 104 alive / 76 gold
- HTTPS: 44 alive / 21 gold
- SOCKS4: 185 alive / 158 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49466
- Ever gold: 1584

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
