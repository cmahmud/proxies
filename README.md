# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 383
- HTTP: 122 alive / 69 gold
- HTTPS: 168 alive / 18 gold
- SOCKS4: 159 alive / 147 gold
- SOCKS5: 169 alive / 149 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40096
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
