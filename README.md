# SyndProxy validated proxy pool

## Current pool

- Alive now: 688
- Gold now: 412
- HTTP: 134 alive / 66 gold
- HTTPS: 187 alive / 12 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40824
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
