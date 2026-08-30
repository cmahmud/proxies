# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 439
- HTTP: 129 alive / 87 gold
- HTTPS: 86 alive / 28 gold
- SOCKS4: 163 alive / 159 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44287
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
