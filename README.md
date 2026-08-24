# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 379
- HTTP: 118 alive / 65 gold
- HTTPS: 45 alive / 12 gold
- SOCKS4: 164 alive / 152 gold
- SOCKS5: 174 alive / 150 gold

## Historical pool

- Discovered: 176968
- Ever alive: 33251
- Ever gold: 1232

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
