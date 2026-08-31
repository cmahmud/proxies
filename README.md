# SyndProxy validated proxy pool

## Current pool

- Alive now: 697
- Gold now: 464
- HTTP: 156 alive / 91 gold
- HTTPS: 139 alive / 36 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 228 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45268
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
