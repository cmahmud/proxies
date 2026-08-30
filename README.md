# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 427
- HTTP: 112 alive / 74 gold
- HTTPS: 71 alive / 27 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 191 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44369
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
