# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 421
- HTTP: 127 alive / 83 gold
- HTTPS: 91 alive / 27 gold
- SOCKS4: 164 alive / 151 gold
- SOCKS5: 189 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44040
- Ever gold: 1392

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
