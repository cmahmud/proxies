# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 422
- HTTP: 114 alive / 79 gold
- HTTPS: 52 alive / 18 gold
- SOCKS4: 163 alive / 160 gold
- SOCKS5: 192 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44497
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
