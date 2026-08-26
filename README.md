# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 392
- HTTP: 133 alive / 72 gold
- HTTPS: 168 alive / 23 gold
- SOCKS4: 155 alive / 145 gold
- SOCKS5: 177 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40004
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
