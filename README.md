# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 392
- HTTP: 129 alive / 72 gold
- HTTPS: 171 alive / 23 gold
- SOCKS4: 158 alive / 147 gold
- SOCKS5: 177 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40084
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
