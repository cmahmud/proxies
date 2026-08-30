# SyndProxy validated proxy pool

## Current pool

- Alive now: 583
- Gold now: 428
- HTTP: 126 alive / 86 gold
- HTTPS: 96 alive / 31 gold
- SOCKS4: 161 alive / 152 gold
- SOCKS5: 200 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44019
- Ever gold: 1388

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
