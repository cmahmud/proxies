# SyndProxy validated proxy pool

## Current pool

- Alive now: 685
- Gold now: 462
- HTTP: 146 alive / 90 gold
- HTTPS: 139 alive / 33 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 227 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45269
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
