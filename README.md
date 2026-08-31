# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 481
- HTTP: 135 alive / 101 gold
- HTTPS: 120 alive / 43 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 199 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45074
- Ever gold: 1423

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
