# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 445
- HTTP: 128 alive / 89 gold
- HTTPS: 72 alive / 33 gold
- SOCKS4: 163 alive / 157 gold
- SOCKS5: 205 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44167
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
