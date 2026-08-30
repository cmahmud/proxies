# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 450
- HTTP: 109 alive / 85 gold
- HTTPS: 46 alive / 29 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 184 alive / 174 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43684
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
