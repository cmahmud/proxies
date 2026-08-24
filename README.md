# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 416
- HTTP: 155 alive / 74 gold
- HTTPS: 73 alive / 18 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 200 alive / 166 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33740
- Ever gold: 1249

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
