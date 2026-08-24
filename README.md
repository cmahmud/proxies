# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 393
- HTTP: 117 alive / 66 gold
- HTTPS: 53 alive / 17 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 181 alive / 153 gold

## Historical pool

- Discovered: 176968
- Ever alive: 33259
- Ever gold: 1232

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
