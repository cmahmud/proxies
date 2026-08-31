# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 420
- HTTP: 86 alive / 59 gold
- HTTPS: 68 alive / 28 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45500
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
