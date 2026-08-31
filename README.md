# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 443
- HTTP: 141 alive / 79 gold
- HTTPS: 109 alive / 29 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 212 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45429
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
