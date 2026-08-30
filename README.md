# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 426
- HTTP: 109 alive / 77 gold
- HTTPS: 47 alive / 23 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44518
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
