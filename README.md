# SyndProxy validated proxy pool

## Current pool

- Alive now: 693
- Gold now: 464
- HTTP: 150 alive / 90 gold
- HTTPS: 141 alive / 34 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 229 alive / 179 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45269
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
