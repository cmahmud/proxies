# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 464
- HTTP: 123 alive / 92 gold
- HTTPS: 52 alive / 29 gold
- SOCKS4: 179 alive / 165 gold
- SOCKS5: 194 alive / 178 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49421
- Ever gold: 1582

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
