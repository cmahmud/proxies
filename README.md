# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 424
- HTTP: 112 alive / 69 gold
- HTTPS: 69 alive / 24 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44410
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
