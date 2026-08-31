# SyndProxy validated proxy pool

## Current pool

- Alive now: 682
- Gold now: 463
- HTTP: 151 alive / 88 gold
- HTTPS: 131 alive / 37 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 228 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45271
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
