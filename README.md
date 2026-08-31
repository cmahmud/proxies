# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 420
- HTTP: 112 alive / 67 gold
- HTTPS: 69 alive / 21 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 205 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45519
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
