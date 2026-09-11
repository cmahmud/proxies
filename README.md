# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 421
- HTTP: 91 alive / 67 gold
- HTTPS: 42 alive / 21 gold
- SOCKS4: 188 alive / 162 gold
- SOCKS5: 179 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48876
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
