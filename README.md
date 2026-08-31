# SyndProxy validated proxy pool

## Current pool

- Alive now: 699
- Gold now: 465
- HTTP: 152 alive / 92 gold
- HTTPS: 139 alive / 33 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 234 alive / 179 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45269
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
