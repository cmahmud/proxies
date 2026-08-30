# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 446
- HTTP: 125 alive / 91 gold
- HTTPS: 74 alive / 35 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 206 alive / 163 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44251
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
