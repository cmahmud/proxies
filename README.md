# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 441
- HTTP: 121 alive / 81 gold
- HTTPS: 132 alive / 33 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 193 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44718
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
