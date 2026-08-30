# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 424
- HTTP: 109 alive / 76 gold
- HTTPS: 55 alive / 20 gold
- SOCKS4: 162 alive / 161 gold
- SOCKS5: 195 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44506
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
