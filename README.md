# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 428
- HTTP: 109 alive / 81 gold
- HTTPS: 54 alive / 22 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44514
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
