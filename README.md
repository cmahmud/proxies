# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 428
- HTTP: 108 alive / 76 gold
- HTTPS: 60 alive / 24 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 191 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44537
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
