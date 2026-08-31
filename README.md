# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 429
- HTTP: 101 alive / 72 gold
- HTTPS: 64 alive / 24 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 195 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45540
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
