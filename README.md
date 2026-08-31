# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 445
- HTTP: 128 alive / 77 gold
- HTTPS: 107 alive / 32 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 219 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45379
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
