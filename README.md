# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 406
- HTTP: 100 alive / 53 gold
- HTTPS: 73 alive / 26 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 192 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45507
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
