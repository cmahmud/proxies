# SyndProxy validated proxy pool

## Current pool

- Alive now: 676
- Gold now: 463
- HTTP: 146 alive / 90 gold
- HTTPS: 133 alive / 34 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 225 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45269
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
