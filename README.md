# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 420
- HTTP: 128 alive / 82 gold
- HTTPS: 90 alive / 27 gold
- SOCKS4: 162 alive / 151 gold
- SOCKS5: 189 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44040
- Ever gold: 1392

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
