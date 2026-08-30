# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 463
- HTTP: 122 alive / 93 gold
- HTTPS: 121 alive / 35 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 205 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44892
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
