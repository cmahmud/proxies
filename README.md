# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 440
- HTTP: 124 alive / 83 gold
- HTTPS: 76 alive / 32 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 185 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44297
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
