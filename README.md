# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 437
- HTTP: 109 alive / 75 gold
- HTTPS: 63 alive / 28 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 203 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45556
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
