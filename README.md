# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 419
- HTTP: 93 alive / 59 gold
- HTTPS: 70 alive / 27 gold
- SOCKS4: 187 alive / 164 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45503
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
