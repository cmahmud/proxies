# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 444
- HTTP: 140 alive / 85 gold
- HTTPS: 77 alive / 34 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 207 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44231
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
