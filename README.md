# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 416
- HTTP: 128 alive / 70 gold
- HTTPS: 76 alive / 20 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33828
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
