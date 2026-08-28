# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 435
- HTTP: 115 alive / 83 gold
- HTTPS: 147 alive / 20 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42330
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
