# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 425
- HTTP: 125 alive / 84 gold
- HTTPS: 92 alive / 29 gold
- SOCKS4: 165 alive / 151 gold
- SOCKS5: 187 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44040
- Ever gold: 1392

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
