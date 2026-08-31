# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 414
- HTTP: 92 alive / 59 gold
- HTTPS: 68 alive / 23 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45504
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
