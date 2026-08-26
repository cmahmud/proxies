# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 389
- HTTP: 134 alive / 72 gold
- HTTPS: 175 alive / 20 gold
- SOCKS4: 157 alive / 145 gold
- SOCKS5: 173 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40001
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
