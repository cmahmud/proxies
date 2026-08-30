# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 449
- HTTP: 125 alive / 82 gold
- HTTPS: 145 alive / 38 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 194 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44744
- Ever gold: 1412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
