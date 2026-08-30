# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 426
- HTTP: 109 alive / 73 gold
- HTTPS: 58 alive / 25 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 200 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44453
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
