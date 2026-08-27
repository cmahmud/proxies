# SyndProxy validated proxy pool

## Current pool

- Alive now: 672
- Gold now: 412
- HTTP: 131 alive / 67 gold
- HTTPS: 172 alive / 15 gold
- SOCKS4: 179 alive / 159 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40835
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
