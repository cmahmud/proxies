# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 420
- HTTP: 108 alive / 76 gold
- HTTPS: 52 alive / 19 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 192 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44512
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
