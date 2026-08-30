# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 445
- HTTP: 143 alive / 88 gold
- HTTPS: 75 alive / 34 gold
- SOCKS4: 163 alive / 158 gold
- SOCKS5: 197 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44283
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
