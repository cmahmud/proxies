# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 423
- HTTP: 128 alive / 84 gold
- HTTPS: 88 alive / 30 gold
- SOCKS4: 161 alive / 151 gold
- SOCKS5: 194 alive / 158 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44032
- Ever gold: 1390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
