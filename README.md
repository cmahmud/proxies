# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 477
- HTTP: 147 alive / 98 gold
- HTTPS: 125 alive / 41 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 193 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45033
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
