# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 446
- HTTP: 141 alive / 88 gold
- HTTPS: 82 alive / 34 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 213 alive / 164 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44209
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
