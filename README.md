# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 424
- HTTP: 96 alive / 69 gold
- HTTPS: 44 alive / 22 gold
- SOCKS4: 195 alive / 162 gold
- SOCKS5: 178 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48878
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
