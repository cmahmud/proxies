# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 382
- HTTP: 126 alive / 62 gold
- HTTPS: 47 alive / 15 gold
- SOCKS4: 171 alive / 152 gold
- SOCKS5: 170 alive / 153 gold

## Historical pool

- Discovered: 176968
- Ever alive: 33252
- Ever gold: 1232

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
