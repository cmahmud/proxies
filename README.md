# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 427
- HTTP: 105 alive / 71 gold
- HTTPS: 60 alive / 23 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 195 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45539
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
