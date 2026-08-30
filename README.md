# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 422
- HTTP: 115 alive / 76 gold
- HTTPS: 44 alive / 20 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 197 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44492
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
