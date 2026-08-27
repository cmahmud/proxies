# SyndProxy validated proxy pool

## Current pool

- Alive now: 684
- Gold now: 408
- HTTP: 133 alive / 62 gold
- HTTPS: 185 alive / 12 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40820
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
