# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 393
- HTTP: 133 alive / 72 gold
- HTTPS: 169 alive / 23 gold
- SOCKS4: 160 alive / 147 gold
- SOCKS5: 175 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40075
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
