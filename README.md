# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 423
- HTTP: 109 alive / 75 gold
- HTTPS: 45 alive / 22 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44523
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
