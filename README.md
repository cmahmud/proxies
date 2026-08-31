# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 425
- HTTP: 108 alive / 66 gold
- HTTPS: 63 alive / 26 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 199 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45539
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
