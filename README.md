# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 446
- HTTP: 128 alive / 86 gold
- HTTPS: 76 alive / 37 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 200 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44128
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
