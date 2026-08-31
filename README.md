# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 412
- HTTP: 93 alive / 59 gold
- HTTPS: 65 alive / 22 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45504
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
