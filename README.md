# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 463
- HTTP: 118 alive / 91 gold
- HTTPS: 116 alive / 36 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 203 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44891
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
