# SyndProxy validated proxy pool

## Current pool

- Alive now: 677
- Gold now: 464
- HTTP: 146 alive / 88 gold
- HTTPS: 132 alive / 37 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 228 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45269
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
