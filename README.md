# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 423
- HTTP: 110 alive / 74 gold
- HTTPS: 59 alive / 25 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44524
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
