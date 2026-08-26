# SyndProxy validated proxy pool

## Current pool

- Alive now: 610
- Gold now: 385
- HTTP: 118 alive / 70 gold
- HTTPS: 164 alive / 20 gold
- SOCKS4: 159 alive / 147 gold
- SOCKS5: 169 alive / 148 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40100
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
