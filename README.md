# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 423
- HTTP: 104 alive / 76 gold
- HTTPS: 60 alive / 21 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44532
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
