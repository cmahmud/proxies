# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 414
- HTTP: 86 alive / 58 gold
- HTTPS: 70 alive / 26 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 191 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45510
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
