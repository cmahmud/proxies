# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 423
- HTTP: 130 alive / 84 gold
- HTTPS: 88 alive / 28 gold
- SOCKS4: 163 alive / 151 gold
- SOCKS5: 186 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44040
- Ever gold: 1392

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
