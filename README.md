# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 423
- HTTP: 109 alive / 79 gold
- HTTPS: 47 alive / 19 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44499
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
