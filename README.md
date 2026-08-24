# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 387
- HTTP: 120 alive / 65 gold
- HTTPS: 59 alive / 15 gold
- SOCKS4: 167 alive / 155 gold
- SOCKS5: 176 alive / 152 gold

## Historical pool

- Discovered: 176968
- Ever alive: 33254
- Ever gold: 1232

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
